from django.shortcuts import render
from .models import Photo, Comment


def pictures_list(request):
    pictures = Photo.objects.all()
    comments = Comment.objects.all()
    return render(request, 'pictures.html', locals())
