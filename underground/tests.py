from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email="test@mail.com",
            password = "secter"
        )
        self.post = Post.objects.create(
            title = "Yengi post",
            body= "Post askldjhf asdihf;asd",
            summary= "Post askldjhf asdihf;asd",
            author = self.user
        )
        def test_string_representaion(self):
            post = Post(title = "Post mavzusi")
            self.assertEqual(str(post), post.title)

        def test_post_content(self):
            self.assertEqual(f'{self.post.title}', "Yangi post matni")
            self.assertEqual(f'{self.post.author}', "Testuser")
            self.assertEqual(f'{self.post.summary}', "summary")
            self.assertEqual(f'{self.post.body}', "Post matni")

        def test_post_list_view(self):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Post matni")
            self.assertTemplateUser(response, 'home.html')
        
        def test_post_detail_view(self):
            response = self.client.get('/post/1')
            no_response = self.client.get('/post/100000/')
            self.assertEqual(response.status_code, 200)
            self.assertContains(no_response, 404)
            self.assertTemplateUser(response, 'My Post')
            self.assertTemplateUser(response, 'post_detail.html')