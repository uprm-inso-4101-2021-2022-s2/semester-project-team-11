from django.test import TestCase
from django.contrib.auth.models import User
from homeservice.models import Job, Listing

# Create your coverage tests here.

class Test_Create_Job(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_listing = Listing.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        testjob = Job.objects.create(
            listing_id=1,
            title='Job Title',
            owner_id=1,
            content='Job Content',
            specialty='Job Specialty',
            slug='Job-title',
            price=100,
            status='incomplete'
        )

    # Test for listing
    def test_listing_content(self):
        job = Job.jobobjects.get(id=1)
        listing = Listing.objects.get(id=1)
        title = f'{job.title}'
        content = f'{job.content}'
        owner = f'{job.owner}'
        specialty = f'{job.specialty}'
        price = f'{job.price}'
        status = f'{job.status}'

        self.assertEqual(owner, 'test_user1')
        self.assertEqual(title, 'Job Title')
        self.assertEqual(content, 'Job Content')
        self.assertEqual(status, 'incomplete')
        self.assertEqual(str(job), "Job Title")
        self.assertEqual(str(listing), "django")