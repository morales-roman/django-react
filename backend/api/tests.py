from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Note
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

class NoteTests(TestCase):
    def setUp(self):
        '''
        Create a test user and authenticate the client.
        '''
        self.user = User.objects.create_user(username='testuser', password='12345')
        refresh = RefreshToken.for_user(self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_note(self):
        '''
        Ensure we can create a new note object.
        '''
        url = reverse('note-list')
        data = {'title': 'Test Note', 'content': 'This is a test note.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Note')

    def test_delete_note(self):
        '''
        Ensure we can delete a note object.
        '''
        note = Note.objects.create(title='Test Note', content='This is a test note.', author=self.user)
        url = reverse('delete-note', kwargs={'pk': note.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)

    def test_get_notes(self):
        '''
        Ensure we can get a list of notes.
        '''
        note = Note.objects.create(title='Test Note', content='This is a test note.', author=self.user)
        url = reverse('note-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Note')
        self.assertEqual(response.data[0]['content'], 'This is a test note.')
        self.assertEqual(response.data[0]['author'], self.user.id)
    
    def test_get_notes_unauthenticated(self):
        '''
        Ensure we can't get a list of notes if unauthenticated.
        '''
        note = Note.objects.create(title='Test Note', content='This is a test note.', author=self.user)
        self.client.credentials()
        url = reverse('note-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

    def test_delete_note_unauthenticated(self):
        '''
        Ensure we can't delete a note object if unauthenticated.
        '''
        note = Note.objects.create(title='Test Note', content='This is a test note.', author=self.user)
        self.client.credentials()
        url = reverse('delete-note', kwargs={'pk': note.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Note.objects.count(), 1)