from django.shortcuts import render, redirect
from .models import Photo, Comment


def pictures_list(request):
    pictures = Photo.objects.all()
    comments = Comment.objects.all()
    return render(request, 'pictures.html', locals())


def picture_details(request, pk):
    picture = Photo.objects.get(pk=pk)
    comments = Comment.objects.filter(photos_id=pk)
    return render(request, 'picture_details.html', locals())


def last_picture(request):
    pictures = Photo.objects.all().order_by("-pub_date")[:3]
    return render(request, 'last_pictures.html', locals())


def comment_picture(request, id):
    picture = Photo.objects.get(id=id)
    comment = request.GET.get("comment", None)
    comm = Comment()
    comm.comments = comment
    comm.photos = picture
    comm.save()
    return redirect("/")
