from django.urls import path
from . import views

app_name = "JobSearch"
urlpatterns = [
    path('',views.Index, name="Index"),
    path('/<str:title>/<str:location>/<int:page_no>', views.Search, name="JobList"),
] 

