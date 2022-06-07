from django.urls import path
from newsletter import views

app_name = 'newsletter'
urlpatterns = [
    path('send_newsletter', views.send_newsletter, name='send_newsletter'),
]
