from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from homeservice.models import Job, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient

# Create your rest framework tests here.
class JobTests(APITestCase):
    def test_view_job(self):
        url = reverse('homeservice_api:listcreate')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_job(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_superuser(
            username='test_user1', password='123456789'
        )
        self.client.login(username=self.testuser1.username, password=self.testuser1.password)

        data = {
            "title": "new",
            "owner": 1,
            "content": "new",
            "price":100
        }
        url = reverse('homeservice_api:listcreate')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_job_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')
        test_job = Job.objects.create(
            title='Job Title', content='Job Content', slug='job-title', owner_id=1, status='incomplete', price=10)

        client.login(username=self.testuser1.username,
                     password='123456789')

        url = reverse(('homeservice_api:detailcreate'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "owner": 1,
                "content": "New",
                "status": "incomplete",
                "price": 100
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)