from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post

class BlogTests(TestCase):
	@classmethod
	def setUp(cls):
		cls.user = get_user_model().objects.create_user(
			username = 'testuser',
			email = 'test@mail.com',
			password = '123456', 
		)
		cls.post = Post.objects.create(
			author = cls.user,
			title = 'Nice post',
			body = 'Nice body content',
		)

	def test_post_model(self):

		self.assertEqual(self.post.author.username,  'testuser')
		self.assertEqual(self.post.title,  'Nice post')
		self.assertEqual(self.posts.body,  'Nice body content')
		self.assertEqual(str(self.post), 'Nice post')