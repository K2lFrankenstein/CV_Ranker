
# @api_view(['POST'])
# def firebase_signup(request):
#     id_token = request.data.get('id_token')
#     try:
#         decoded_token = auth.verify_id_token(id_token)
#         uid = decoded_token['uid']
#         user, created = User.objects.get_or_create(username=uid)
#         if created:
#             # Add additional user info if needed
#             user.save()
#         login(request, user)
#         return Response({"message": "User signed up successfully"}, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



# firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
# authe = firebase.auth()
# database=firebase.database()


import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
import pyrebase

from CV_Ranker.settings import FIREBASE_CONFIG,BASE_DIR







cred_path = os.path.join(BASE_DIR,'randomsearch-b73d9-firebase-adminsdk-49jaq-198ac8941e.json')

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)


if not firebase_admin._apps:
    firebase_admin.initialize_app()



@api_view(['POST'])
def firebase_login(request):
    
    ussr = request.data.get('User')
    final_token = ussr['stsTokenManager']["accessToken"]
    email = ussr['email']
    # print(f"Received id_token: {ussr}")

    try:
        decoded_token = firebase_auth.verify_id_token(final_token)
        uid = decoded_token['uid']
        # print(f"Decoded UID: {uid}")

        # Create or get the user
        user,created = User.objects.get_or_create(username=email, last_name = uid)
        login(request, user)
        print(f"User Created: ------------- {created}")
        
        some_path = email.split('@')[0]
        base_dir_cv = os.path.join(BASE_DIR,"uploaded_files","CV",some_path)
        base_dir_jd = os.path.join(BASE_DIR,"uploaded_files","JD",some_path)

        os.makedirs(base_dir_cv, exist_ok=True)
        os.makedirs(base_dir_jd, exist_ok=True)

        # Redirect the user to the dashboard
        return Response({"message": "User signed up successfully"}, status=status.HTTP_201_CREATED)

    except Exception as e:

        print(f"Error verifying token: {e}")

        return Response({"message": "Error logging in user"}, status=status.HTTP_400_BAD_REQUEST)


def firebase_logout(request):
    # logout(request) part of working 
    uid = str(request.user.last_name)

    # print(uid,type(uid))

    # Revoke the user's refresh tokens
    firebase_auth.revoke_refresh_tokens(uid)

    # Logout the user from Django's session
    logout(request)
    return redirect('/')




def login_page(request):
    

    if request.user.is_authenticated:
        return redirect('../dashboard')
            
    else: 
        return render(request, "login.html")







