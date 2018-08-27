from django.contrib import admin

from .models import Tweet, Message, Comment


def change_flag(model_admin, request, queryset):
    for obj in queryset:
        if obj.flag == False:
            obj.flag = True
        else:
            obj.flag = False
        obj.save()


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['content', 'creation_date', 'user']
    actions = [change_flag]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'content', 'creation_date', 'was_read']
    actions = [change_flag]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'tweet', 'content', 'creation_date']
    actions = [change_flag]
