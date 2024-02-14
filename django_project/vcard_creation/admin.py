from vcard_creation.models import VCardModel
from django.contrib import admin


class VCardModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(VCardModel, VCardModelAdmin)
