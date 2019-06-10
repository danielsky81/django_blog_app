from django.shortcuts import render
from .models import Post

# Create your views here.
def get_todo_list(request):
    results = Post.objects.all()
    return render(request, 'posts.html', {'posts': results})
