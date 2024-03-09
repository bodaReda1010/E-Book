from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [

    path('',views.home,name='home'),
    path('<str:category_slug>/',views.home,name='category_slug'),

]