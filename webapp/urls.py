from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
     path('index/', views.say_hello),
     path('services/', views.services_tab),
     path('login/', views.loginPage),
     path('register/', views.registerPage),
]
