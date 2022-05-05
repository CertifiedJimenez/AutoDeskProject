from django.urls import path
from . import views

app_name = "JobSearch"
urlpatterns = [
    path('',views.index, name="Index"),
    path('Search',views.Search,name="Search"),
    path('Search/<str:title>/<str:location>', views.JobList, name="JobList"),
    path('Search/<str:title>/<str:location>/<int:Id>', views.JobPage, name="JobPage")
] 