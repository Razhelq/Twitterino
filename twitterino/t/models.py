from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=1024)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    flag = models.BooleanField(default=False)

    @property
    def name(self):
        return "{} {}".format(self.user, self.creation_date)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='msg_sender', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(User, related_name='msg_recipient', on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1024)
    creation_date = models.DateTimeField(auto_now=True)
    was_read = models.BooleanField(default=False)
    flag = models.BooleanField(default=False)


class Comment(models.Model):
    sender = models.ForeignKey(User, related_name='cmt_sender', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(User, related_name='cmt_recipient', on_delete=models.DO_NOTHING)
    tweet = models.ForeignKey(Tweet, related_name='tweet', on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1024)
    creation_date = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=False)
