from django.urls import path
from . import views

app_name = "JobListing"
urlpatterns = [
    path('/<int:type>/<int:Id>', views.Listing, name="Listing")
] 
