

from django.shortcuts import render

def post_list(request):
    return render(request, 'shine/post_list.html')
