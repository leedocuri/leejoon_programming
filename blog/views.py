from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.forms import CommentModelForm
from blog.models import Post, Comment

def post_list(request):
    return render(request, 'blog/post_list.html',
        {})

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/list.html',
        {'post_list' : post_list})

def comment_new(request):
    if request.method =='POST':
        form = CommentModelForm(request.POST, request)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentModelForm()

    return render(request, 'blog/comment_form.html', {'form':form,
        })

def comment_edit(request, pk):
    comment = Comment.objects.get(pk = pk)
    if request.method =='POST':
        form = CommentModelForm(request.POST, request,instance = comment)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentModelForm(instance=comment)

    return render(request, 'blog/comment_form.html',
        {'form':form,
        })


