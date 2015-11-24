from django.shortcuts import render
from .models import Group, MemberShip


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', locals())
