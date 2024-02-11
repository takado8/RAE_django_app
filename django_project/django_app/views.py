from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('create_vcard')


@login_required
def create_vcard(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        organization = request.POST.get('organization')
        website = request.POST.get('website')
        notes = request.POST.get('notes')

        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Address: {address}")
        print(f"Phone: {phone}")
        print(f"Organization: {organization}")
        print(f"Website: {website}")
        print(f"Notes: {notes}")

        return HttpResponse("VCard created successfully!")
    else:
        return render(request, 'create_vcard.html')
