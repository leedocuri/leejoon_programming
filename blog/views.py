from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.forms import CommentModelForm

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def comment_new(request):
    if request.method =='POST':
        form = CommentModelForm(request.POST, request,FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentModelForm()

    return render(request, 'blog/comment_form.html', {'form':form,
        })
