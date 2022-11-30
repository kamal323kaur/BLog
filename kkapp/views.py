from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})
def nextt(request):
    return render(request,'back.html',{})
def about(request):
    return render(request,'about.html',{})
def contact(request):
    return render(request,'contact.html',{})    
def post(request):
    return render(request,'post.html',{})
def createpost(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        text = request.POST.get("text")
        user = Post(author = request.user, title =title, text = text, published_date =timezone.now())
        user.save()
        return redirect("/")
    return render(request,'contact.html',{})   
def deletepost(request,id):
    usr = Post.objects.get(id = id)
    usr.delete()
    return redirect("/")     
def updatepost(request, id):
    pt = Post.objects.get(id = id)
    if request.method == 'POST':
        title = request.POST.get('tit')
        text = request.POST.get('text')
        pt.title = title
        pt.text = text
        pt.save()
        return redirect('/')
    return render(request,'update.html',{'pt':pt})

def registeruser(request):
    frm=UserCreationForm()
    if request.method == "POST":
            frm=UserCreationForm(request.POST)
            if frm.is_valid():
                frm.save()
                return redirect('/')        
    return render(request, "register.html",{'frm':frm})


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        print(username, password)
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request,'login.html',{})
def logoutuser(request):
    logout(request)
    return redirect('login')
