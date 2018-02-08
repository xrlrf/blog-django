# coding:utf-8

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    sex = models.CharField(max_length=5)
    signature = models.CharField(max_length=80)

    def __unicode__(self):
        return self.username

class PubHeader(models.Model):
	id = models.OneToOneField(Publisher,on_delete = models.CASCADE,primary_key = True)
	url = models.FileField(upload_to = 'pubheader')


class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
