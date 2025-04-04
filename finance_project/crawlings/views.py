from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    return render(request,"crawlings/index.html")

def delete_comment(request):

    return 