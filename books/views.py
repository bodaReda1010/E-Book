from django.shortcuts import render
from .models import Category , Book
def home(request , price_sold = 0 , price_rental = 0 , category_slug = None):
    if category_slug != None:
        category = Category.objects.get(slug=category_slug)
        books = Book.objects.filter(category = category , active = True)
    else:
        books = Book.objects.all().filter(active = True)

        
    categories = Category.objects.all()
    sold_books = Book.objects.filter(status = 'sold')
    rental_books = Book.objects.filter(status = 'rental')
    for book in sold_books:
        price_sold += book.price

    for r in rental_books:
        price_rental += r.total_rental

    total = price_sold + price_rental



    context = {
        'books' : books,
        'categories' : categories,
        'total':total,

    }
    return render(request , 'home/home.html' , context)