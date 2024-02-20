from django.shortcuts import render
from django.http import HttpResponse
from .models import data
# Create your views here.
def home(request):
    users = data.objects.all()
    print(users, "#USERS")
    return render(request,"home.html",{"users":users}) 