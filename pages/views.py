from django.shortcuts import render
"""from .models import Team

teams = Team.objects.all()
data = {
    'teams': teams,
}"""


# Create your views here.
def dashboard(request):
    return render(request, 'pages/dashboard.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def service(request):
    return render(request, 'pages/service.html')
