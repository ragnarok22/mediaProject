from django.db.models.query_utils import Q

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .models import Group, MemberShip


def group_list(request):
    groups = Group.objects.all()
    members = MemberShip.objects.all()
    return render(request, 'group_list.html', locals())


def group_detail(request, pk):
    group = Group.objects.get(pk=pk)
    members = MemberShip.objects.filter(group_id=pk)
    return render(request, 'group_detail.html', locals())


def create_group(request):
    name = request.GET.get("name-group", None)
    about = request.GET.get("about-group", None)
    if name is not None and about is not None:
        exist = Group.objects.filter(name=name)
        if exist:
            sms = "ese grupo ya existe"
            return render(request, 'create_group.html', locals())
        group = Group(name=name, about=about, owner=request.user)
        group.save()
        return redirect(reverse('account:dashboard'))
    else:
        return render(request, 'create_group.html', locals())


def join_group(request, id):
    group = Group.objects.get(id=id)
    member = MemberShip(group=group, person=request.user, inviter=request.user, invite_reason="")
    exist = MemberShip.objects.filter(Q(person=request.user) | Q(group=group))
    if not exist:
        member.save()
    return redirect("/")
