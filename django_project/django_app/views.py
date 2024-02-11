from django.shortcuts import render
from django.http import HttpResponse


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

        # Do something with the form data (e.g., create a vCard)
        # For demonstration purposes, let's just print the data to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Address: {address}")
        print(f"Phone: {phone}")
        print(f"Organization: {organization}")
        print(f"Website: {website}")
        print(f"Notes: {notes}")

        # Optionally, you can return a response indicating success
        return HttpResponse("VCard created successfully!")
    else:
        # If the request method is not POST, render the form template
        return render(request, 'create_vcard.html')
