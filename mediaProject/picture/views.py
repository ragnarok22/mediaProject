from django.shortcuts import render
from .models import Photo


def pictures_list(request):
    pictures = Photo.objects.all()
    return render(request, 'pictures.html', locals())
