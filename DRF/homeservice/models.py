from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    class JobObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='incomplete')

    options = (
        ('incomplete', 'Incomplete'),
        ('fulfilled', 'Fulfilled')
    )

    listing = models.ForeignKey(Listing, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_post')
    content = models.TextField(null=True)
    specialty = models.CharField(max_length=128)
    price = models.IntegerField()
    status = models.CharField(max_length=10, choices=options, default='incomplete')
    slug = models.SlugField(max_length=250, unique_for_date='posted')
    posted = models.DateTimeField(default=timezone.now)
    objects = models.Manager() # default manager
    jobobjects = JobObjects()

    class Meta:
        ordering = ('-posted',)

    def __str__(self):
        return self.title