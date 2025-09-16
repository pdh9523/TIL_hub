from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            nickname='테스트유저'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.nickname, '테스트유저')
        self.assertTrue(self.user.check_password('testpass123'))

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_follower_count_property(self):
        user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        self.user.followers.add(user2)
        self.assertEqual(self.user.follower_count, 1)

    def test_following_count_property(self):
        user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        user2.followers.add(self.user)
        self.assertEqual(self.user.following_count, 1)

    def test_follow_relationship(self):
        user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        user3 = User.objects.create_user(
            username='testuser3',
            email='test3@example.com',
            password='testpass123'
        )

        user2.followers.add(self.user)
        user3.followers.add(self.user)

        self.assertEqual(self.user.following_count, 2)
        self.assertEqual(user2.follower_count, 1)
        self.assertEqual(user3.follower_count, 1)


class UserAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            nickname='테스트유저'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123',
            nickname='테스트유저2'
        )

    def test_user_signup(self):
        url = reverse('accounts:signup')
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123',
            'nickname': '새유저'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

    def test_user_signup_duplicate_username(self):
        url = reverse('accounts:signup')
        data = {
            'username': 'testuser',
            'email': 'new@example.com',
            'password': 'newpass123',
            'nickname': '새유저'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_list(self):
        url = reverse('accounts:user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_user_detail_get(self):
        url = reverse('accounts:user_detail', kwargs={'user_id': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_detail_get_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:user_detail', kwargs={'user_id': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_user_update_by_owner(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:user_detail', kwargs={'user_id': self.user.id})
        data = {
            'nickname': '수정된닉네임'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.nickname, '수정된닉네임')

    def test_user_update_by_other_user(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('accounts:user_detail', kwargs={'user_id': self.user.id})
        data = {
            'nickname': '수정된닉네임'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_delete_by_owner(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:user_detail', kwargs={'user_id': self.user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 1)

    def test_user_delete_by_other_user(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('accounts:user_detail', kwargs={'user_id': self.user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_follow_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:follow', kwargs={'user_id': self.user2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], '팔로우했습니다.')
        self.assertTrue(self.user in self.user2.followers.all())

    def test_unfollow_user(self):
        self.user2.followers.add(self.user)
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:follow', kwargs={'user_id': self.user2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], '팔로우를 취소했습니다.')
        self.assertFalse(self.user in self.user2.followers.all())

    def test_follow_self(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:follow', kwargs={'user_id': self.user.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], '자기 자신을 팔로우할 수 없습니다.')

    def test_follow_unauthenticated(self):
        url = reverse('accounts:follow', kwargs={'user_id': self.user2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_follow_nonexistent_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:follow', kwargs={'user_id': 999})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'nickname': '테스트유저'
        }

    def test_user_serializer_create(self):
        from .serializers import UserSerializer
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass123'))

    def test_user_serializer_password_write_only(self):
        from .serializers import UserSerializer
        user = User.objects.create_user(**self.user_data)
        serializer = UserSerializer(user)
        self.assertNotIn('password', serializer.data)

    def test_user_list_serializer_fields(self):
        from .serializers import UserListSerializer
        user = User.objects.create_user(**self.user_data)
        serializer = UserListSerializer(user)
        expected_fields = {'id', 'username', 'nickname', 'follower_count', 'following_count'}
        self.assertEqual(set(serializer.data.keys()), expected_fields)
