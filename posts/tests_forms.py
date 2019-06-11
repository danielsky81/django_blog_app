from django.test import TestCase
from .forms import PostForm

# Create your tests here.
class TestToDoPostForm(TestCase):
    def test_can_create_an_post(self):
        form = PostForm({'title': 'Create Test', 'content': 'blab bla'})
        self.assertTrue(form.is_valid)

    def test_correct_message_for_missing_title(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])