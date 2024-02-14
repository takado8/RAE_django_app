from django.shortcuts import render
from django.http import HttpResponse
import vobject
from vcard_creation.models import VCardModel


def vcard_main_view(request, vcard_id, username):
    if request.method == 'POST':
        # Handle form submission
        phone_number = request.POST.get('phone')

        return HttpResponse("Form submitted successfully!")
    else:
        vcard = VCardModel.objects.get(id=vcard_id)
        context = {
            'data': {
                'vcard_id': vcard_id,
                'name': vcard.name,
                'img_url': vcard.image.url,
                'organization': vcard.organization
            }
        }
        return render(request, 'vcard_main.html', context=context)


def download_vcf(request, vcard_id):
    # Generate vCard
    vcard_model = VCardModel.objects.get(id=vcard_id)
    vcard = vobject.vCard()
    vcard.add('fn').value = vcard_model.name
    vcard.add('org').value =[vcard_model.organization]
    vcard.add('tel').value = vcard_model.phone
    vcard.add('email').value = vcard_model.email
    # Serve vCard as attachment
    response = HttpResponse(vcard.serialize(), content_type='text/vcard')
    response['Content-Disposition'] = 'attachment; filename="contact.vcf"'
    return response
