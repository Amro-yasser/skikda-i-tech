from django.shortcuts import render

# Create your views here.
def formations(request):
    return render (request, 'formations.html',{})