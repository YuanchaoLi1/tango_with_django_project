from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect

# Ex7
def add_category(request): 
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST) 

        if form.is_valid():

            cat = form.save(commit=True)
            print(cat, cat.slug)
            return redirect('/rango/')
        else:  
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


# E5/6
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None 
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)

def index(request):
    # Ex5/6
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    
    return render(request, 'rango/index.html', context_dict)


    # Ex4
    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

    # Ex3
    return HttpResponse ("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>" )

def about(request):  
    # Ex4
    # context_dictAbout = {'boldmessage': 'This tutorial has been put together by Yuanchao Li.'}
    # return render(request, 'rango/about.html')

    # Ex3
    return HttpResponse("Rango says here is the about page.<br/> <a href='/rango/'>Index</a>")
    