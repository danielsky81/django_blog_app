from django.test import TestCase
from .models import Post

class TestPostModel(TestCase):
    def test_post_as_a_string(self):
        post = Post(title = 'Create a Test')
        self.assertEqual('Create a Test', str(post))