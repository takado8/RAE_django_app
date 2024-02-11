from django.urls import path
from django_app.views import create_vcard
from django_app.views import CustomLoginView


urlpatterns = [
    path('', create_vcard, name='create_vcard'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]
