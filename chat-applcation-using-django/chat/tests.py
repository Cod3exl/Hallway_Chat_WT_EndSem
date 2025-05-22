from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile, Contact, Message

class ChatModelTests(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='testuser1', password='password123')
        self.user2 = User.objects.create_user(username='testuser2', password='password123')
        
        # Create a contact relationship
        self.contact = Contact.objects.create(user=self.user1, contact=self.user2)
        
        # Create a test message
        self.message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content='Hello, this is a test message'
        )
    
    def test_profile_creation(self):
        """Test that profiles are automatically created for users"""
        self.assertTrue(hasattr(self.user1, 'profile'))
        self.assertTrue(hasattr(self.user2, 'profile'))
    
    def test_contact_relationship(self):
        """Test contact relationship between users"""
        self.assertIn(self.user2, [contact.contact for contact in self.user1.contacts.all()])
        self.assertNotIn(self.user1, [contact.contact for contact in self.user2.contacts.all()])
    
    def test_message_creation(self):
        """Test message creation and properties"""
        self.assertEqual(self.message.sender, self.user1)
        self.assertEqual(self.message.receiver, self.user2)
        self.assertEqual(self.message.content, 'Hello, this is a test message')
        self.assertFalse(self.message.is_read)

class ChatViewTests(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='testuser1', password='password123')
        self.user2 = User.objects.create_user(username='testuser2', password='password123')
        
