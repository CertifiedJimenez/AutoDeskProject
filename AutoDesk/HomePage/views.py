from django.shortcuts import redirect, render

# Create your views here.

def Index(request):
    return render(request,'HomePage/Index.html')

