from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from homeservice.models import Job, Category
from django.contrib.auth.models import User

# Create your rest framework tests here.
class JobTests(APITestCase):
    def test_view_job(self):
        url = reverse('homeservice_api:listcreate')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_job(self):
        self.test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        data = {
            "title": "new",
            "owner": 1,
            "content": "new",
            "price":100
        }
        url = reverse('homeservice_api:listcreate')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
