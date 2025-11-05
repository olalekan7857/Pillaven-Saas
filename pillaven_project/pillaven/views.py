from django.shortcuts import render
from .forms import ReviewForm
from .models import *
from django.http import JsonResponse

from django.core.mail import send_mail

# Create your views here.

def index(request):
    allprojects = Projects.objects.order_by('-id')

    context = {
        'allprojects': allprojects
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'page-about.html')

def projects(request):
    allprojects = Projects.objects.order_by('-id')

    context = {
        'allprojects': allprojects
    }
    return render(request, 'page-projects.html', context)

def team(request):
    return render(request, 'page-team.html')


def contact(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()  

            
            subject = f"New Review from {review.name} - {review.subject}"
            message = (
                f"Source: saas.pillaven.com\n\n"
                f"You have received a new review message fr:\n\n"
                f"Name: {review.name}\n"
                f"Email: {review.email}\n"
                f"Phone: {review.phone_number}\n\n"
                f"Message:\n{review.message}"
            )

            try:
                # Send email to support mailbox
                send_mail(
                    subject,
                    message,
                    "support@pillaven.com",  # From (your verified sender)
                    ["support@pillaven.com"],  # To (where you want to receive messages)
                    fail_silently=False,
                )

                return JsonResponse({
                    'status': 'true',
                    'message': 'Your message was sent successfully!'
                })
            except Exception as e:
                return JsonResponse({
                    'status': 'false',
                    'message': f'Error sending email: {e}'
                })

    else:
        form = ReviewForm()

    context = {'form': form}
    return render(request, 'page-contact.html', context)



def pillaven(request, slug):
    myslug = Projects.objects.get(slug = slug)
    allprojects = Projects.objects.order_by('-id')

    context = {
        'myslug': myslug,
        'allprojects' : allprojects
    }
    return render(request, 'project-detail.html', context)