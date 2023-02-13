from django.shortcuts import render


def home(request):
    headline = 'Ala ma kota 😎'
    return render(request, template_name='home/home.html', context={'title': headline})


def contact(request):
    return render(request, template_name='home/contact.html')
