from django.shortcuts import render
from books.models import Category , Book
def home(request):
    books = Book.objects.all().filter(active = True)
    categories = Category.objects.all().filter(active = True)
    context = {
        'books' : books,
        'categories' : categories,
    }
    return render(request , 'home/home.html' , context)