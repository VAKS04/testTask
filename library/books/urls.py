from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name="index"),
    path('add_book/',add_book,name="add_book"),
    path('list_books/',list_books,name="list_books"),
    path('delete_book/',delete_book,name="delete_book"),
    path('book_search/',book_search,name="book_search"),
    path('change_status/',change_status,name="change_status"),
    path('change_status_page/<int:int_pk>',change_status_page,name="change_status_page")
]