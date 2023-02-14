from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('messages/', views.messages, name='messages'),
    path('messages/<int:pk>/', views.message, name='message'),
    path('messages/delete/<int:pk>', views.message_delete, name='message_delete'),
]
