from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Book
from .forms import *

#Базавая страница при входе
def index(request):
    return render(request,"books/index.html")


#Страница для отоброжения всех книг 
def list_books(request):
    books = Book.objects.all()

    return render(request,"books/list_books.html",{'books':books})

#Страница для отображения всех книг с ссылками на изминение их статуса
def change_status(request):
    books = Book.objects.all()
    return render(request,"books/change_status.html",{"books":books})

#Страница для изменения статуса книги
def change_status_page(request,int_pk):
    book = get_object_or_404(Book, id=int_pk)
    data = {
        "title":book.title,
        "author":book.author,
        "year":book.year
    }
    if request.method == 'POST':
        form = BookStatusForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Перенаправление на список книг или другую страницу
    else:
        form = BookStatusForm(instance=book)
    return render(request,"books/change_status_page.html",{"form":form,"book":data})


#Страница для удаления книги на страницы
def delete_book(request):
    books = Book.objects.all()

    if request.method=="POST":
        id =request.POST.get("id",None)
        if id is not None:
            try:
                book = get_object_or_404(Book,pk = int(id))
                book.delete()
                return redirect("delete_book")
                
            except Exception as e:
                return HttpResponse(f"{e}")
            
    return render (request,"books/delete_book.html",{'books':books})
        # form = DeleteBookForm(request.POST)
        # if form.is_valid():


#Функция для проверки поля на его содержание
def isNotEmptyField(value):
    if isinstance(value, int):
        return value != 0
    return bool(str(value).strip())

 #Функция для фильтрации книг
def filterBooks(title,author,year):

    book = Book.objects.all()

    if isNotEmptyField(title):
        book = book.filter(title = title)
    elif isNotEmptyField(author):
        book = book.filter(author = author)
    elif isNotEmptyField(year):
        try:
            year = int(year)
            book = book.filter(year = year)
        except ValueError:
            pass
    return book


#Страница для нахождения книги по 3 ключам 
def book_search(request):
    title = request.GET.get('title',None)
    author = request.GET.get('author',None)
    year = request.GET.get('year',None)
    result = filterBooks(title,author,year)

    return render(request,"books/book_search.html",{"books":result})

#Страница для добавления книги 
def add_book(request):
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BooksForm()
    return render(request,"books/add_book.html",{'form':form})
# Create your views here.
