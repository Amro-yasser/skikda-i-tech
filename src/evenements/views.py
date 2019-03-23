from django.shortcuts import render

def evenements(request):
    return render (request, 'evenements.html',{})