from django.urls import path
from users.views import RegisterAPIView, LoginAPIView
from knox.views import LogoutView


urlpatterns = [
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]