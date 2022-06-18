from django.shortcuts import redirect, render
from APIControl.views import ReedDetailsAPI, LibraryDetailsAPI



# Create your views here.
def Listing(request,type,Id):    
    match type:
        case 1:
            JobContext = ReedDetailsAPI(request,Id)
        case 2:
            JobContext = LibraryDetailsAPI(request,Id)

    #Template Context
    context = {'job': JobContext}
    return render(request,'JobListing/Listing.html',context)