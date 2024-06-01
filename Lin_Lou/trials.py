# import os
# import json
# import requests
# import firebase_admin
# import firebase_admin.auth as auth
# from firebase_admin import credentials
# from rest_framework import authentication


# cred = credentials.Certificate("static/fir-auth-with-django-firebase-adminsdk-1zepn-3023fd129c.json")
# firebase_admin.initialize_app(cred)
# FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")
# rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"


# def create_user(email, password):
#     """
#     Function for creating firebase user.
#     """
#     created_user = auth.create_user(email=email, password=password)
#     return created_user.uid


# def change_firebase_user_password(new_password, uid):
#     """
#     Function for changing password of firebase user.
#     """
#     auth.update_user(uid, password=new_password)


# def change_firebase_user_email(uid, new_email):
#     """
#     Function for change email of firebase user.
#     """
#     auth.update_user(uid, email=new_email)


# def delete_firebase_user(uid):
#     """
#     Function for deleting firebase user.
#     """
#     auth.delete_user(uid)


# def login_firebase_user(email, password):
#     """
#     Function for login firebase user.
#     """
#     payload = json.dumps({
#     "email": email,
#     "password": password,
#     "returnSecureToken": True
#     })

#     r = requests.post(rest_api_url,
#     params={"key": FIREBASE_WEB_API_KEY},
#     data=payload)
#     return r.json()


# def logout_firebase_user(uid):
#     auth.revoke_refresh_tokens(uid)


# class FirebaseAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         from users.models import CustomUser
#         token = request.headers.get('Authorization')
#         if not token:
#          return None

#         try:
#             token = token.split(" ")[1]
#             decoded_token = auth.verify_id_token(token, check_revoked=True)
#             uid = decoded_token["uid"]
#         except:
#             return None

#         try:
#             user = CustomUser.objects.get(uid=uid)
#             return user, None

#         except CustomUser.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         from users.models import CustomUser
        
#         try:
#             return CustomUser.objects.get(id=user_id)
#         except CustomUser.DoesNotExist:
#             return None





# --------------------------------------------------------------------------