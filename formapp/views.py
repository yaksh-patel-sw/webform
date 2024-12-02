from django.http import JsonResponse
from django.shortcuts import render
from .models import Registration
from .forms import ContactForm
import random
import string

def generate_link():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if Registration.objects.filter(email=email).exists() or Registration.objects.filter(phone=phone).exists():
            return JsonResponse({'message': 'Email or Phone already exists!'}, status=400)
        view_link = f"https://streamyard.com/{generate_link()}"
        Registration.objects.create(
            name=request.POST.get('name'),
            email=email,
            phone=phone,
            accepted_terms=True,
            view_link=view_link
        )
        return JsonResponse({'message': 'Registration successful!', 'view_link': view_link})
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # Retrieve form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']
            accepted_terms = form.cleaned_data['accepted_terms']

            # Handle the form submission logic (save data or send email)
            # You can store the phone number and accepted terms as needed
            
            # Assuming a successful form submission
            return JsonResponse({'message': 'Form submitted successfully!'})

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


