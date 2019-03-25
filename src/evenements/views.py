from django.shortcuts import render
from .models import Event


def evenements(request):
    
    most_recent = Event.objects.order_by('-timestamp')[:1]
    event_list = Event.objects.all()
    

    context = {
        'most_recent':most_recent,
        'even_list':event_list,
    }
    
    
    return render (request, 'evenements.html',{})


def events_details(request):
    return render (request, 'events_details.html',{})