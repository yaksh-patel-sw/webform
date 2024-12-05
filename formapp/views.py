import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Registration
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
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
    

def home(request):
    if request.method == 'POST':
        # Get form data from the request body
        data = json.loads(request.body)
        email = data.get('email')
        phone = data.get('phone')

        # Check if the email or phone already exists
        if Registration.objects.filter(email=email).exists() or Registration.objects.filter(phone=phone).exists():
            return JsonResponse({'message': 'Email or Phone already exists!'}, status=400)

        # Generate the view link
        view_link = f"https://streamyard.com/{generate_link()}"
        
        # Create the registration
        Registration.objects.create(
            name=data.get('name'),
            email=email,
            phone=phone,
            accepted_terms=True,
            view_link=view_link
        )

        # Return success response with view link
        return JsonResponse({'message': 'Registration successful!', 'view_link': view_link})



