
from django.urls import path
from django_app.views import create_vcard

urlpatterns = [
    path('', create_vcard, name='create_vcard')
]
