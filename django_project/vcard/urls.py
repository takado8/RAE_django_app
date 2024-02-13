from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from vcard.views import vcard_main_view, download_vcf


urlpatterns = [
    path('vcard', vcard_main_view, name='vcard_main_view'),
    path('download_vcf', download_vcf, name='download_vcf'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
