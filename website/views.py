from django.shortcuts import render,HttpResponse,redirect
from api.models import *

def check(request):
    p=request.META["REMOTE_ADDR"]
    if(p=="127.0.0.1"):
        return redirect("sdfgdfjklgnklsdfjmgklsdfkldfgkldfmngkldfnm/")
    return render(request,"404.html",{})