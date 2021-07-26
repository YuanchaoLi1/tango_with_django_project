from django.conf.urls import include
from django.urls import path
from rango import views

app_name ='rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('about/', include('about.urls')),
    # path('about/', <a href='/rango/about'>About</a>, name='about'),
]