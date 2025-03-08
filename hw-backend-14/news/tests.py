from django.test import TestCase, Client
from django.urls import reverse
from .models import News, Comment

# Create your tests here.

class NewsModelTests(TestCase):

    def test_has_comments_true(self):
        news = News.objects.create(title="Test News", content="Test content")
        Comment.objects.create(news=news, content="Test comment")
        self.assertTrue(news.has_comments())

    def test_has_comments_false(self):
        news = News.objects.create(title="Test News", content="Test content")
        self.assertFalse(news.has_comments())



class NewsViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.news1 = News.objects.create(title="News 1", content="Content 1")
        self.news2 = News.objects.create(title="News 2", content="Content 2")
        Comment.objects.create(news=self.news1, content="Comment 1")
        Comment.objects.create(news=self.news1, content="Comment 2")

    def test_news_list_order(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context['news_with_likes'],
            [{'news': self.news2, 'likes_count': 0}, {'news': self.news1, 'likes_count': 0}],
            transform=lambda x: {'news': x['news'], 'likes_count': x['likes_count']}
        )

    def test_news_detail(self):
        response = self.client.get(reverse('news_detail', args=[self.news1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['news'], self.news1)

    def test_news_detail_comments_order(self):
        response = self.client.get(reverse('news_detail', args=[self.news1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context['comments'],
            list(self.news1.comment_set.order_by('-created_at'))
        )