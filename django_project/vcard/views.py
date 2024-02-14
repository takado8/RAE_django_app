from django.shortcuts import render, redirect
from django.http import HttpResponse
import vobject
from vcard_creation.models import VCardModel
from vcard.ceremeo_client import post_lead


def vcard_main_view(request, vcard_id, username):
    if request.method == 'POST':
        # Handle form submission
        phone_number = request.POST.get('phone')
        request.session['lead'] = {
            'phone_number': phone_number,
        }
        post_lead(phone_number)
        return redirect('vcard_page_2')
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


def vcard_page_2(request):
    if request.method == 'POST':
        # Handle form submission
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        organization = request.POST.get('organization')
        phone_number = request.session.get('lead')['phone_number']
        name_split = fullname.split()
        name = name_split[0]
        surname = None
        if len(name_split) > 1:
            surname = name_split[1]

        post_lead(phone_number, name=name, surname=surname, email=email,
            comments=[{'organization': organization}])
        return redirect('vcard_page_3')
    else:
        return render(request, 'vcard_page_2.html')


def vcard_page_3(request):
    if request.method == 'POST':
        # Handle form submission
        date = request.POST.get('date')
        text_input = request.POST.get('text_input')
        phone_number = request.session.get('lead')['phone_number']
        comments = []
        if date:
            comments.append({'preferred_date': str(date)})
        if text_input:
            comments.append({'preferred_topic': text_input})

        post_lead(phone_number, comments=comments if comments else None)
        return HttpResponse("Form submitted successfully!")
    else:
        return render(request, 'vcard_page_3.html')
