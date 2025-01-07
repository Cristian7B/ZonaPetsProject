from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path('register/', UserRegister.as_view(), name='register'),
	path('login/', UserLogin.as_view(), name='login'),
	path('logout/', UserLogout.as_view(), name='logout'),
	path('user/', UserView.as_view(), name='user'),
    path("get_user_info/", GetUserInfo.as_view(), name="get_user_info"),
	path("update_user_info/", UpdateUserInfo.as_view(), name="update_user_info"),
    path("google_token/", GoogleLoginToken.as_view(), name="token_google"),
    path("google_credential/", GoogleLoginCredential.as_view(), name="credential_google"),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]