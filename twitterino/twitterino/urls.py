"""twitterino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from t.views import BaseView, IndexView, AddTweetView, LoginView, LogoutView, UserTweetsView, TweetDetailsView
from t.views import UserMessagesView, SendMessageView, MessageDetailsView, AddCommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', BaseView.as_view(), name='base'),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^add_tweet/$', AddTweetView.as_view(), name='add-tweet'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^user_tweets/(?P<id>(\d)+)/$', UserTweetsView.as_view(), name='user-tweets'),
    url(r'^tweet_details/(?P<id>(\d)+)/$', TweetDetailsView.as_view(), name='tweet-details'),
    url(r'^user_messages/(?P<id>(\d)+)/$', UserMessagesView.as_view(), name='user-messages'),
    url(r'^send_message/(?P<id>(\d)+)/$', SendMessageView.as_view(), name='send-message'),
    url(r'^message_details/(?P<id>(\d)+)/$', MessageDetailsView.as_view(), name='message-details'),
    url(r'^add_comment/(?P<id>(\d)+)/$', AddCommentView.as_view(), name='add-comment')
]
