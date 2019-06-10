from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def get_todo_list(request):
    results = Post.objects.all()
    return render(request, 'posts.html', {'posts': results})

def create_an_item(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = PostForm()

        # new_post = Post()
        # new_post.title = request.POST.get('title')
        # new_post.content = request.POST.get('content')
        # new_post.save()
        # return redirect(get_todo_list)

    return render(request, 'item_form.html', {'form': form})

def edit_an_post(request, id):
    post = get_object_or_404(Post, pk = id)

    if request.method == "POST":
        form = PostForm(request.POST, instance = post)  
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = PostForm(instance = post)

    return render(request, 'item_form.html', {'form': form})