from django.test import TestCase, Client
from django.urls import reverse

from .models import Post

HOME_URL_REVERSE = reverse('home')
HOME_URL = '/'

class PostModelTests(TestCase):
    def setUp(self):
        self.test_text = 'A test post.'
        Post.objects.create(text=self.test_text)
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.text, self.test_text)


class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        Post.objects.create(text='A test post.')
    
    def test_view_url_exist_at_proper_location(self):
        res = self.client.get(HOME_URL)
        self.assertEqual(res.status_code, 200)
    
    def test_view_url_by_name(self):
        res = self.client.get(HOME_URL_REVERSE)
        self.assertEqual(res.status_code, 200)
    
    def test_view_use_correct_template(self):
        res = self.client.get(HOME_URL_REVERSE)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')


