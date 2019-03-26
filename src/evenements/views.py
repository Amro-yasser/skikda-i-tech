from django.shortcuts import render
from .models import Event
from .forms import PostForm
from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



def evenements(request):
    
    most_recent = Event.objects.order_by('-timestamp')[:1]
    event_list = Event.objects.order_by('-timestamp')[1:]
    

    context = {
        'most_recent':most_recent,
        'event_list':event_list,
    }
    
    
    return render (request, 'evenements.html',context)


def events_details(request,id):
    most_recent = Event.objects.order_by('-timestamp')[:3]
    event = get_object_or_404(Event,id=id)
    ps = Event.objects.all()
    
    

    context = {
        'ps':ps,
        'most_recent':most_recent,
        'event':event,
        
    }
    return render (request, 'events_details.html',context)