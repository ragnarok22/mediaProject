from django.contrib.auth.models import User
from django.db import models


def url(self, filename):
    route = 'users/%s/%s' % (self.user.username, filename)
    return route


class UserProfile(models.Model):

    photo = models.ImageField(upload_to=url)
    about_me = models.TextField()
    sign = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name='profile')
    born_date = models.DateField()
    SEX_CHOICES = (
        ('M', 'Masculino'),
        ('W', 'Femenino'),
        ('U', 'Sin definir'),
    )
    CIVIL_STATUS_CHOICES = (
        ('M', 'casado'),
        ('S', 'soltero'),
        ('F', 'con novia'),
        ('C', 'es complicado'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='U')
    civil_status = models.CharField(max_length=1, choices=CIVIL_STATUS_CHOICES, default='S')
    is_conected = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Friendship(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='+')
    receiver = models.ForeignKey(UserProfile)
    STATUS_CHOICE = (
        ('0', 'Accepted'),
        ('1', 'Denied'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    date = models.DateField()

    def __str__(self):
        return '%s want be a friend to %s' % (self.sender.user.first_name, self.receiver.user.first_name)
