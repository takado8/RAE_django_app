from django.shortcuts import render
from django.http import HttpResponse
import vobject


def vcard_main_view(request):
    if request.method == 'POST':
        # Handle form submission
        phone_number = request.POST.get('phone')

        return HttpResponse("Form submitted successfully!")
    else:
        return render(request, 'vcard_main.html')


def download_vcf(request):
    # Generate vCard
    vcard = vobject.vCard()
    vcard.add('fn').value = 'John Doe'
    vcard.add('tel').value = '111222333'

    # Serve vCard as attachment
    response = HttpResponse(vcard.serialize(), content_type='text/vcard')
    response['Content-Disposition'] = 'attachment; filename="contact.vcf"'
    return response
