from django.shortcuts import render
from django.utils import timezone
from shine.models import Post

def Post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'shine/Post_list.html', {'posts': posts})

