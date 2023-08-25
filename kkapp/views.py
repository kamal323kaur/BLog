from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

def index(request):
    items_per_page = 5
    posts = Post.objects.all()
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    current_page = paginator.get_page(page_number)
    return render(request,'index.html',{'current_page': current_page})

@login_required
def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('comment', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})


@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return redirect('comment_list') 

  
@login_required
def createpost(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        text = request.POST.get("text")
        user = Post(author = request.user, title =title, text = text, published_date =timezone.now())
        user.save()
        return redirect("/")
    return render(request,'add_post.html',{})   
@login_required
def deletepost(request,id):
    usr = Post.objects.get(id = id)
    usr.delete()
    return redirect("/")  

@login_required   
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


