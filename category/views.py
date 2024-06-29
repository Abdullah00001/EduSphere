from django.shortcuts import render
from category.models import CategoryModel
from book.models import BookModel

# Create your views here.


def CategoriesBookView(request, category_name):
    context = {}
    category = CategoryModel.objects.get(category_name=category_name)
    books = BookModel.objects.filter(book_category=category)
    context["books"] = books
    return render(request, "category/books_by_category.html", context)
