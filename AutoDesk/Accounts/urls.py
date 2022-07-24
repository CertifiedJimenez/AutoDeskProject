from django.urls import path
from . import views

app_name = "Accounts"
urlpatterns = [
    path('login/',views.login, name="login"),
] 