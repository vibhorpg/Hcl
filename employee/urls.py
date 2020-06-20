
from .views import EmployeeView
from django.urls import path

urlpatterns = [
    #list,create
    path('', EmployeeView.as_view()),

    #get employee,update,delete
    path('<int:pk>', EmployeeView.as_view()),
]
