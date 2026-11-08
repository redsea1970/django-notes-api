from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note


class NoteAPITests(APITestCase):
    def setUp(self):
        # Создаем двух пользователей для теста изоляции
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        
        # Создаем заметку для первого пользователя
        self.note1 = Note.objects.create(title='Note 1', text='Text 1', author=self.user1)

    def test_create_user(self):
        """Проверка регистрации пользователя"""
        url = reverse('register')  # Убедись, что у тебя есть такой url, если нет — мы это исправим
        data = {'username': 'newuser', 'password': 'newpassword123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_create_note_authenticated(self):
        """Проверка создания заметки авторизованным пользователем"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('note-list')
        data = {'title': 'New Note', 'text': 'New Text'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)

    def test_list_notes_only_own(self):
        """Проверка, что пользователь видит только свои заметки"""
        self.client.force_authenticate(user=self.user2)
        url = reverse('note-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # user2 не должен видеть заметки user1

    def test_unauthorized_access(self):
        """Проверка, что без авторизации доступ закрыт"""
        url = reverse('note-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
