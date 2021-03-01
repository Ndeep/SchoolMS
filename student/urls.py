from django.urls import  path,re_path
from student.views import update_profile


urlpatterns=[
        path('/profile', update_profile,name='student profile'),
]