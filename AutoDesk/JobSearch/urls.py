from django.urls import path
from . import views

app_name = "JobSearch"
urlpatterns = [
    path('',views.index, name="Index"),
    path('Search',views.Search,name="Search"),
    path('Search/<str:title>/<str:location>/<int:page_no>', views.JobList, name="JobList"),
    path('Listing/<str:title>/<str:location>/<int:Id>', views.JobPage, name="Listing")
] 