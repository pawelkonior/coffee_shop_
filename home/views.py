from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


def home(request):
    headline = 'Ala ma kota 😎'
    return render(request, template_name='home/home.html', context={'title': headline})


def contact(request):
    return render(request, template_name='home/contact.html')


def messages(request):
    msgs = models.Contact.objects.all()
    return render(request, 'home/messages.html', {'messages': msgs})


def message(request, pk):
    msg = models.Contact.objects.get(pk=pk)
    return render(request, 'home/message.html', {'message': msg})


def message_delete(request, pk):
    models.Contact.objects.get(pk=pk).delete()
    return redirect(reverse('home:messages'))
