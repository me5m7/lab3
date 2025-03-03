from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def links_page(request):
    return render(request, 'links.html')
def text_formatting_page(request):
    return render(request, 'text_formatting.html')