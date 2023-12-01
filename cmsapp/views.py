from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .forms import PostForm
from .models import Post



# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
    'posts':posts
    }
    return render(request, "cmsapp/index.html" ,context)

def detail(request,slug):
    post = Post.objects.get(slug =slug)
    posts = Post.objects.exclude(post_id = post.post_id)
    context = {
        'post':post,
        'posts': posts
    }
    return render(request,"cmsapp/detail.html",context)


def createdForm(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            messages.info(request,'The Article is successfully created')
            return redirect('create')
        else:
            messages.error(request, 'The Article is successfully created')
    context ={
        'form': form
    }
    return render(request,'cmsapp/create.html', context)

def updateForm(request, slug):
     post = Post.objects.get(slug=slug)
     form = PostForm(instance=post)
     if request.method =='POST':
         form = PostForm(request.POST, request.FILES,instance=post)
         if form.is_valid():
             form.save()
             return redirect('detail')
     context ={
            'form':form
     }
     return  render(request,'cmsapp/create.html', context)


def deleteForm(request, slug):
    post = Post.objects.get(slug=slug)
    form =PostForm(instance=post)
    if request.method =='POST':
        post.delete()
        return redirect('index')

    context = {
        'form':form
    }
    return render(request, 'cmsapp/delete.html', context)

