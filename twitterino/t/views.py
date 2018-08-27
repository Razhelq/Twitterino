from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from t.models import Tweet, Message, Comment

from t.forms import TweetForm, LoginForm, SendMessageForm, AddCommentForm


class BaseView(View):

    def get(self, request):
        return render(request, 'base.html')


class IndexView(View):

    def get(self, request):
        if request.user.is_authenticated:
            tweets = Tweet.objects.filter(flag=False)
            return render(request, 'index.html', {'tweets': tweets})
        return redirect('login')


class AddTweetView(View):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            form = TweetForm()
            return render(request, 'add_tweet.html', {'form': form, 'user': user})
        return redirect('login')

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            user = request.user
            Tweet.objects.create(content=form.cleaned_data['content'], user=user)
        return redirect('index')


class UserTweetsView(View):

    def get(self, request, id):
        if request.user.is_authenticated:
            tweets = Tweet.objects.filter(user__id=id).filter(flag=False)
            user = User.objects.get(id=id)
            return render(request, 'user_tweets.html', {'tweets': tweets, 'user': user})
        return redirect('login')


class LoginView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
        return redirect('index')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')
        return redirect('/')


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('index')
        return redirect('login')


class TweetDetailsView(View):

    def get(self, request, id):
        if request.user.is_authenticated:
            tweet = Tweet.objects.get(id=id)
            comments = Comment.objects.filter(tweet__id=id).filter(flag=False)
            return render(request, 'tweet_details.html', {'tweet': tweet, 'comments': comments})
        return redirect('login')

class UserMessagesView(View):

    def get(self, request, id):
        if request.user.is_authenticated:
            user = User.objects.get(id=id)
            sent_messages = Message.objects.filter(sender=user).filter(flag=False)
            recieved_messages = Message.objects.filter(recipient=user).filter(flag=False)
            return render(request, 'user_messages.html', {
                'sent': sent_messages,
                'recieved': recieved_messages
            })
        return redirect('login')

class SendMessageView(View):

    def get(self, request, id):
        sender = request.user
        if sender.is_authenticated:
            recipient = User.objects.get(id=id)
            form = SendMessageForm()
            return render(request, 'send_message.html', {'form': form, 'sender': sender, 'recipient': recipient})
        return redirect('login')

    def post(self, request, id):
        recipient = User.objects.get(id=id)
        sender = User.objects.get(id=id)
        form = SendMessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                sender=sender,
                recipient=recipient,
                content=form.cleaned_data['content']
            )
            return redirect('user-messages', id)
        return redirect('login')


class MessageDetailsView(View):

    def get(self, request, id):
        if request.user.is_authenticated:
            message = Message.objects.get(id=id)
            message.was_read = True
            message.save()
            return render(request, 'message_details.html', {'message': message})
        return redirect('login')


class AddCommentView(View):

    def get(self, request, id):
        if request.user.is_authenticated:
            tweet = Tweet.objects.get(id=id)
            form = AddCommentForm()
            return render(request, 'add_comment.html', {'form': form, 'tweet': tweet})
        return redirect('login')

    def post(self, request, id):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            tweet = Tweet.objects.get(id=id)
            Comment.objects.create(
                sender=request.user,
                recipient=tweet.user,
                tweet=tweet,
                content=form.cleaned_data['content']
            )
            return redirect('tweet-details', id)
        return redirect('index')













