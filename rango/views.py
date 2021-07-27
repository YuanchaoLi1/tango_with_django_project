from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # Ex4
    # Construct a dictionary to pass to the template engine as its context.
    # context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return render(request, 'rango/index.html', context=context_dict)

    # Ex3
    return HttpResponse ("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>" )

def about(request):  
    # Ex4
    # context_dictAbout = {'boldmessage': 'This tutorial has been put together by Yuanchao Li.'}
    # return render(request, 'rango/about.html')

    # Ex3
    return HttpResponse("Rango says here is the about page.<br/> <a href='/rango/'>Index</a>")
    