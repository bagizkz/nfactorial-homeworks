from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment, Like
from .forms import NewsForm, CommentForm


# Create your views here.

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    news_with_likes = []
    for item in news:
        likes_count = item.like_set.count()
        news_with_likes.append({'news': item, 'likes_count': likes_count})
    return render(request, 'news/news_list.html', {'news_with_likes': news_with_likes})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comment_set.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'news/news_detail.html', {'news': news, 'comments': comments, 'form': form})

def news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})

def add_like(request, pk):
    news = get_object_or_404(News, pk=pk)
    Like.objects.create(news=news)
    return redirect('news_detail', pk=pk)