from django.shortcuts import render
from django.views.generic import ListView
from .models import Message

# def MessageView(request):
#     return render (request,'home.html')

class MessageView(ListView):
    model = Message
    template_name = 'home.html'