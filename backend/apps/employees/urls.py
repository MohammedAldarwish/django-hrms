from django.urls import path
from .views import EmployeeView

urlpatterns = [
    path("emp", EmployeeView.as_view(), name="emp")
]