from django.urls import path 
from .views import CourseFunc



urlpatterns = [
    
    path('' , CourseFunc.as_view() , name = 'coursefunc')
]
