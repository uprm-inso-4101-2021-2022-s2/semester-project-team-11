from django.contrib import admin
from .import models

# Register your models here.
@admin.register(models.Job)
class OwnerAdmin(admin.ModelAdmin):
    job_display = ('title', 'id','owner', 'content', 'category', 'price', 'status')
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(models.Category)