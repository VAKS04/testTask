from django import forms
from .models import Book


class BooksForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"


class BookStatusForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['status']

# class DeleteBookForm(forms.Form):
#     id_book = forms.IntegerField()