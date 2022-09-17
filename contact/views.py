from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from django.shortcuts import render
from .models import contactlist
from .models import contactform
from django.conf import settings


# Create your views here.

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactformdata = contactform(name=name, email=email, message=message, subject=subject)
        contactformdata.save()

        context = {
            'name': name,
            'email': email,
            'message': message

        }

        send_mail(
            name,
            subject,  # subject
            message,  # message
            # email,  # form_email
            # settings.EMAIL_HOST_USER, # from email
            ['soumodip432@gmail.com'],  # to_email
            fail_silently=False
        )
        return render(request, 'contact.html', context=context)
    else:
        return render(request, 'contact.html', {})
