from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    import datetime
    now = datetime.datetime.now()
    context = {}
    context['time'] = now
    return render(request, 'runoob.html', context)

