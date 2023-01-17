from django.test import TestCase
from user.models import User
from .models import Post, Category


class Create_Post_Test(TestCase):
    
    """Create Testcase So We Can Coverage Our Model"""
    
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='test')
        TestUser = User.objects.create_user(email="hakimov@gmail.com",first_name="hakimov",user_name="hakimov", password="19992020")
        TestPost = Post.objects.create(category_id=1,
                                       title="Test Post Title",
                                       excerpt="Test Post Excerpt",
                                       content="Test Post Content",
                                       slug="Post-test-title",
                                       author_id=1,
                                       status="published")
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f"{post.author}"
        excerpt = f"{post.excerpt}"
        title = f"{post.title}"
        content = f"{post.content}"
        status = f"{post.status}"
        self.assertEqual(author, "hakimov")
        self.assertEqual(title, "Test Post Title")
        self.assertEqual(content, "Test Post Content")
        self.assertEqual(status, "published")
        self.assertEqual(str(post), "Test Post Title")
        self.assertEqual(str(cat), "test")