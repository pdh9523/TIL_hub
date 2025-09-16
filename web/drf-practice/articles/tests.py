from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Article, Comment

User = get_user_model()


class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.article = Article.objects.create(
            title='Test Article',
            content='Test content',
            author=self.user
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.content, 'Test content')
        self.assertEqual(self.article.author, self.user)

    def test_article_str_representation(self):
        self.assertEqual(str(self.article), 'Test Article')

    def test_article_ordering(self):
        article2 = Article.objects.create(
            title='Second Article',
            content='Second content',
            author=self.user
        )
        articles = Article.objects.all()
        self.assertEqual(articles[0], article2)
        self.assertEqual(articles[1], self.article)


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.article = Article.objects.create(
            title='Test Article',
            content='Test content',
            author=self.user
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author=self.user,
            content='Test comment content'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.article, self.article)
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.content, 'Test comment content')

    def test_comment_str_representation(self):
        expected = f'{self.article.title} - Test comment content'
        self.assertEqual(str(self.comment), expected)


class ArticleAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        self.article = Article.objects.create(
            title='Test Article',
            content='Test content',
            author=self.user
        )

    def test_get_article_list(self):
        url = reverse('articles:article_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_article_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('articles:article_list_create')
        data = {
            'title': 'New Article',
            'content': 'New content'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 2)

    def test_create_article_unauthenticated(self):
        url = reverse('articles:article_list_create')
        data = {
            'title': 'New Article',
            'content': 'New content'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_article_detail(self):
        url = reverse('articles:article_detail', kwargs={'article_id': self.article.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Article')

    def test_update_article_by_author(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('articles:article_detail', kwargs={'article_id': self.article.id})
        data = {
            'title': 'Updated Article',
            'content': 'Updated content'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Updated Article')

    def test_update_article_by_other_user(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('articles:article_detail', kwargs={'article_id': self.article.id})
        data = {
            'title': 'Updated Article',
            'content': 'Updated content'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_article_by_author(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('articles:article_detail', kwargs={'article_id': self.article.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Article.objects.count(), 0)

    def test_delete_article_by_other_user(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('articles:article_detail', kwargs={'article_id': self.article.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        self.article = Article.objects.create(
            title='Test Article',
            content='Test content',
            author=self.user
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author=self.user,
            content='Test comment'
        )

    def test_get_comment_list(self):
        url = reverse('articles:comment_list_create', kwargs={'article_id': self.article.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_comment_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('articles:comment_list_create', kwargs={'article_id': self.article.id})
        data = {
            'content': 'New comment'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_create_comment_unauthenticated(self):
        url = reverse('articles:comment_list_create', kwargs={'article_id': self.article.id})
        data = {
            'content': 'New comment'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_comment_by_author(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('articles:comment_detail', kwargs={'comment_id': self.comment.id})
        data = {
            'content': 'Updated comment'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated comment')

    def test_update_comment_by_other_user(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('articles:comment_detail', kwargs={'comment_id': self.comment.id})
        data = {
            'content': 'Updated comment'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_comment_by_author(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('articles:comment_detail', kwargs={'comment_id': self.comment.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)

    def test_delete_comment_by_other_user(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('articles:comment_detail', kwargs={'comment_id': self.comment.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
