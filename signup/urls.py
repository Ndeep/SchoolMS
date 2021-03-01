from django.urls import path
from signup.views import signup

urlpatterns=[
    path('signup',signup,name='register')
]