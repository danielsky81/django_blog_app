from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Post

class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "posts.html")

    def test_get_add_post_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_post_page(self):
        post = Post(title = 'Create a Test')
        post.save()
        page = self.client.get("/edit/{0}".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_page_for_post_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        # no post created in test scenario so there is no post with id = 1

    # def test_post_create_an_item(self):
    #     response = self.client.post('/add', {'title': 'Create a Test'})
    #     post = get_object_or_404(Post, pk = 1)
    #     self.assertEqual(post, 'Create a Test')