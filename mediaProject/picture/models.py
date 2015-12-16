from django.db import models
from django.contrib.auth.models import User


def url(self, filename):
    route = 'pictures/%s/%s' % (self.owner, filename)
    return route


class Photo(models.Model):
    owner = models.ForeignKey(User)
    picture = models.ImageField(upload_to=url)
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return "%s del usuario %s" % (self.title, self.owner)


class Comment(models.Model):
    comments = models.TextField()
    photos = models.ForeignKey(Photo)

    def __str__(self):
        return "%s --> %s" % (self.comments, self.photos)

