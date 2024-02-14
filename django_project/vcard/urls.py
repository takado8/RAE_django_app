from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from vcard.views import vcard_main_view, download_vcf, vcard_page_2


urlpatterns = [
    path('<str:vcard_id>/<str:username>', vcard_main_view, name='vcard_main_view'),
    path('vcard/download_vcf/<str:vcard_id>', download_vcf, name='download_vcf'),
    path('vcard_page_2', vcard_page_2, name='vcard_page_2'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
