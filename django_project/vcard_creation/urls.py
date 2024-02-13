from django.urls import path
from vcard_creation.views import create_vcard, result_url_page
from vcard_creation.views import CustomLoginView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', create_vcard, name='create_vcard'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('vcard_result', result_url_page, name='vcard_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
