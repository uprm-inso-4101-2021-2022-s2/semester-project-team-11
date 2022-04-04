from django.urls import path
from django.views.generic import TemplateView

app_name = 'homeservice'

urlpatterns = [
    path('', TemplateView.as_view(template_name="homeservice/index.html")),
]
