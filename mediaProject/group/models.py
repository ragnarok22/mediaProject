from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    members = models.ManyToManyField(User, through='MemberShip', through_fields=('group', 'person'), related_name='members_group')

    def __str__(self):
        return self.name


class MemberShip(models.Model):
    group = models.ForeignKey(Group)
    person = models.ForeignKey(User)
    inviter = models.ForeignKey(User, related_name='membership_invites')
    invite_reason = models.CharField(max_length=100)

    def __str__(self):
        return "%s --> %s" % (self.group, self.person)