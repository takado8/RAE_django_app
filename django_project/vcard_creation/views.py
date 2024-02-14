from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from vcard_creation.models import VCardModel
from vcard_creation.vcard_url_service import generate_qr_img, generate_url


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('create_vcard')


@login_required
def create_vcard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        organization = request.POST.get('organization')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        website = request.POST.get('website')
        image = request.FILES.get('image')
        vcard = VCardModel.objects.create(
            name=name,
            organization=organization,
            phone=phone,
            email=email,
            website=website,
            image=image
        )
        # Store data in session
        request.session['vcard_data'] = {
            'vcard_id': vcard.id,
            'name': name,
            'organization': organization,
            'phone': phone,
            'email': email,
            'website': website,
            'image_path': vcard.image.url if image else None
        }
        print(f"Name: {name}")
        print(f"Organization: {organization}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print(f"Website: {website}")
        if image:
            print(f"Image: {vcard.image.url}")

        return redirect('vcard_result')
    else:
        return render(request, 'create_vcard.html')


def result_url_page(request):
    vcard_url = generate_url(request)
    qr_image = generate_qr_img(vcard_url)
    context = {
        'data': {
            'qr_image': qr_image,
            'url': vcard_url,
        }
    }
    return render(request, 'result_url_page.html', context)


