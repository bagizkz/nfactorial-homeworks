from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment, Like
from .forms import NewsForm, CommentForm, SignUpForm
from django.views import View
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import News
from .serializers import NewsSerializer
from django.shortcuts import get_object_or_404

# Create your views here.




class NewsListCreateAPIView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsDetailAPIView(APIView):
    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def delete(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "news/sign_up.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, _ = Group.objects.get_or_create(name="default")
            user.groups.add(group)
            return redirect("login")
        return render(request, "news/sign_up.html", {"form": form})


def news_list(request):
    news = News.objects.all().order_by('-created_at')
    news_with_likes = []
    for item in news:
        likes_count = item.like_set.count()
        news_with_likes.append({'news': item, 'likes_count': likes_count})
    return render(request, 'news/news_list.html', {'news_with_likes': news_with_likes})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comment_set.all().order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.author = request.user
            comment.save()
            return redirect('news_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'news/news_detail.html', {'news': news, 'comments': comments, 'form': form})



@login_required
def news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})


def add_like(request, pk):
    news = get_object_or_404(News, pk=pk)
    Like.objects.create(news=news)
    return redirect('news_detail', pk=pk)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        news = get_object_or_404(News, pk=self.kwargs['pk'])
        return self.request.user == news.author or self.request.user.groups.filter(name='moderators').exists()

    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        form = NewsForm(instance=news)
        return render(request, 'news/news_update.html', {'form': form, 'news': news})

    def post(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_detail', pk=pk)
        return render(request, 'news/news_update.html', {'form': form, 'news': news})
    


@login_required
def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    
    if request.user == news.author or request.user.groups.filter(name='moderators').exists():
        news.delete()
        return redirect('news_list')
    
    return redirect('news_detail', pk=pk)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.user == comment.author or request.user.groups.filter(name='moderators').exists():
        comment.delete()
        return redirect('news_detail', pk=comment.news.pk)

    return redirect('news_detail', pk=comment.news.pk)