from django.urls import path
from accounts.api import UserApi, LoginApi, RegisterApi, UserAuthApi
from knox import views as knox_views

urlpatterns = [
    path('', UserApi.as_view()),
    path('user', UserAuthApi.as_view()),
    path('login', LoginApi.as_view()),
    path('register', RegisterApi.as_view()),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]