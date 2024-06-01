import os,json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ETL import utils
from .forms import FileFieldForm
from django.views.decorators.csrf import csrf_exempt
from ETL.models import *
from CV_Ranker.settings import BASE_DIR

json_file_path = os.path.join(BASE_DIR,"ETL",'smt_files.json')

# main dashboard 
def dashboard(request):
    if request.user.is_authenticated:
            return render(request, "home.html")
    else: 

        return redirect("/")


     
# CV and Job description upload 
def upload_page(request):
    if request.method == 'POST':
        form = FileFieldForm(request.POST, request.FILES)
        
        email = str(request.user)
        some_path = email.split('@')[0]

        if form.is_valid():

            # saving from the cv part of form 
            cv_file = request.FILES.getlist('file_field')
            for file in cv_file:
                handle_uploaded_file(file,some_path)


            # saving from the JD part of form
            job_description = form.cleaned_data.get('job_description')
            job_description_file = request.FILES.get('job_description_file')
            job_title = form.cleaned_data.get('job_title')
            
            if job_description:
                
                print(f"Job Title: {job_title}")
                print(f"Job Description: {job_description}")

                job_details = {
                               "Job Title": job_title,
                                "Job Description": job_description
                            }

                job_details_json = json.dumps(job_details, indent=4)

                file_path = os.path.join(BASE_DIR, "uploaded_files", "JD",some_path,job_title+".json")

                with open(file_path, 'w') as file:
                        file.write(job_details_json)
                
                temp1={
                    "filename": job_title,
                    "extension": ".txt",
                    "is_cv": False,
                    "is_jd": True,
                    "Job Tittle":job_title
                }

            elif job_description_file:
                
                handle_uploaded_file_jobdescript(job_description_file,some_path)

                filename, extension = os.path.splitext(job_description_file.name)


                temp1={
                    "filename": filename,
                    "extension": extension,
                    "is_cv": False,
                    "is_jd": True,
                    "Job Tittle":job_title
                }



            ListOfFILES= []

            ListOfFILES.append(temp1)

            for i in cv_file:
                fil, ext = os.path.splitext(i.name)
                temp={
                    "filename": fil,
                    "extension": ext,
                    "is_cv": True,
                    "is_jd": False,

                }

                ListOfFILES.append(temp)

           

            global json_file_path
            
            with open(json_file_path, 'r') as json_file:
                try:
                    ds_ls = json.load(json_file)
                except json.JSONDecodeError:
                    # If the file is empty or corrupted, initialize with an empty dictionary
                    ds_ls = {}

            
            ds_ls[email]=ListOfFILES

            with open(json_file_path, 'w') as json_file:
                json.dump(ds_ls, json_file)

            request.session["job_title"] = "fresh"
            return render(request, "uploading.html", {"ListOfFILES": ListOfFILES, "msg": "Files Uploaded succesfully","upd":1})
    
        else:
             return render(request, "uploading.html", {"form": form, "upd": 0,})
    
    else:
        form = FileFieldForm()
    return render(request, "uploading.html", {"form": form,"upd":0})

def handle_uploaded_file(file,some_path):

    cv_file_path = os.path.join(BASE_DIR, "uploaded_files", "CV",some_path)
    os.makedirs(cv_file_path, exist_ok=True)

    
    with open(os.path.join(cv_file_path, file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def handle_uploaded_file_jobdescript(file,some_path):

    JD_file_path = os.path.join(BASE_DIR, "uploaded_files", "JD",some_path)
    os.makedirs(JD_file_path, exist_ok=True)
    with open(os.path.join(JD_file_path, file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)






# CV and job description processing unit :
def processed(request):
    if "job_title" in request.session:
        
        print(request.session["job_title"])
        if request.session["job_title"] == "fresh":

            global json_file_path
            with open(json_file_path, 'r') as json_file:
                    smt_data = json.load(json_file)


            email = str(request.user)
            some_path = email.split('@')[0]
            path_to_cv = os.path.join(BASE_DIR, "uploaded_files", "CV",some_path)
            path_to_jd = os.path.join(BASE_DIR, "uploaded_files", "JD",some_path)
            
            list_data_file = smt_data.get(email, "Something went wrong please re-Upload the files")

            formatted_data = utils.file_handeller(list_data_file,path_to_cv,path_to_jd,email) 
            print(formatted_data)

            request.session["job_title"] = "old"


            tp_path = os.path.join(BASE_DIR, "ETL", "temp_processed.json")

            with open(tp_path, 'r') as json_file:
                try:
                    tp_data = json.load(json_file)
                except json.JSONDecodeError:
                    # If the file is empty or corrupted, initialize with an empty dictionary
                    tp_data = {}

            tp_data[email]=formatted_data

            with open(tp_path, 'w') as tp:
                json.dump(tp_data, tp)

            final_ans = []
            f_key = User.objects.get(username = email)
            for objs in formatted_data:
                
                
                final_ans.append(StructuredFormate.objects.get(id=objs,UID = f_key))


            return render(request, "processed.html",{"data":final_ans,"test":""})
             
        elif request.session["job_title"] == "old":
          
            tp_path = os.path.join(BASE_DIR, "ETL", "temp_processed.json")

            with open(tp_path, 'r') as json_file:
                tp_data = json.load(json_file)

            final_ans = []
            
            email = str(request.user)
            f_key = User.objects.get(username = email)
            print(f_key,f_key.id,type(f_key))

            for objs in tp_data[email]:
                
                final_ans.append(StructuredFormate.objects.get(id=objs,UID = f_key))


            return render(request, "processed.html",{"data":final_ans,"test":""})

            
    
    else : 
        data={}
        test = "enter some files first"
        return render(request, "processed.html",{"data":data,"test":test})



def master(request):

    email = str(request.user)

    f_key = User.objects.get(username = email)
    data = StructuredFormate.objects.filter(UID = f_key)
    
    print("query set",data)

    return render(request, "master.html",{"data":data})




def structure(request,id):
    if request.method == 'GET':

        
        
        # print(id,type(title),type(score))
        # email = str(request.user)
        # f_key = User.objects.get(username = email)

        # jd_key = JobDescription.objects.filter(UID = f_key,jobTittle = title)
        # if len(jd_key) != 0:
        #         jd_key = jd_key[0]

        # print("=--------dasdasd-",jd_key)

        raw_data = StructuredFormate.objects.get(id = id)
        
        print(raw_data)

        final_data = {
            "resumeName": raw_data.resumeName
        }

        ls = ["skills", "contactInfo", "experience", "others", "project", "education"]

        for key in ls:
            temp = getattr(raw_data, key)
            if temp != "NAN":
                json_string = json.dumps(temp, indent=None, separators=(',', ': '))
                formatted_string = ' | '.join(json_string[1:-1].split(','))
                formatted_string = formatted_string.replace("'", "")
                formatted_string = formatted_string.replace('"', "")
                # print(key, " -- ", formatted_string)
                # print("\n")

                final_data[key] = formatted_string
        


        print("=---------",final_data)



        return render(request, "single_view.html",{"data":final_data})
    
    return JsonResponse({'status': 'fail', 'message': 'Only GET requests are allowed'}, status=400)
    