from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
   return HttpResponse("Hello World, you are at the index of my web")

def about(request):
   return render_to_response('about_us.html',{'title':'about'})

def home(request):
   return render_to_response('home.html', {'title':'home'})

def help(request):
   return render_to_response('help.html', {'title':'help'})
