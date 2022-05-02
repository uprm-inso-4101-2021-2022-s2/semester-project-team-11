from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Add category field ???
class Job(models.Model):
    class JobObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='incomplete')

    options = (
        ('incomplete', 'Incomplete'),
        ('fulfilled', 'Fulfilled')
    )
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_post')
    content = models.TextField(null=True)
    price = models.IntegerField()
    status = models.CharField(max_length=10, choices=options, default='incomplete')
    time = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(max_length=250, unique_for_date='time')
    objects = models.Manager() # default manager
    jobobjects = JobObjects()

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return self.title