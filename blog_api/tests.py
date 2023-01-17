from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from blog.models import Post, Category
from user.models import User

class PostTest(APITestCase):
    def test_view_post(self):
        """
          Ensure That The Posts are Accessed Correctly
        """
        url = reverse("listCreate")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_post(self):
        """
          Ensure That The Posts are being Created In API
        """
        self.test_category = Category.objects.create(name="test")
        self.Testuser1 = User.objects.create_superuser(email="hakimov@gmail.com",first_name="hakimov",user_name="hakimov", password="19992020")
        
        self.client.login(email=self.Testuser1.email, password="19992020")
        
        data = {"title": "news",
                "author": self.Testuser1.id,
                "excerpt": "new",
                "category":self.test_category.id,
                "content": "new",
                }
        url = reverse("listCreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        def test_post_update(self):
            client = APIClient()
            self.test_category = Category.objects.create(name="Test_cat")
            self.TestUser1 = User.objects.create_user(email="hakimov@gmail.com",first_name="hakimov",user_name="hakimov", password="19992020")
            self.TestUser2 = User.objects.create_user(email="petrenkov@gmail.com",first_name="petrenkov",user_name="petri", password="19992020")
            
            client.login(email="petrenkov@gmail.com", password="19992020")
            url = reverse(("detailcreate"), kwargs={"pk": 1})
            
            response = client.put(
                url, {
                    "title": "new",
                    "author": self.Testuser1.id,
                    "category": self.test_category.id,
                    "excerpt": "New",
                    "content": "new Content",
                    "status": "published",
                }
                , format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_200_OK)
