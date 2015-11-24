from django.shortcuts import render
from .models import Group, MemberShip


def group_list(request):
    groups = Group.objects.all()
    members = MemberShip.objects.all()
    return render(request, 'group_list.html', locals())


def group_detail(request, pk):
    group = Group.objects.get(pk=pk)
    members = MemberShip.objects.filter(group_id=pk)
    return render(request, 'group_detail.html', locals())
