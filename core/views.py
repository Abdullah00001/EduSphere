from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from category.models import CategoryModel
from book.models import BookModel

# Create your views here.


class HomePageView(ListView):
    template_name = "core/index.html"
    model = BookModel

    def get_books_by_category_name(self, category_name):
        return BookModel.objects.filter(book_category__category_name=category_name)[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["fictions"] = self.get_books_by_category_name("Fiction")
        context["nonfictions"] = self.get_books_by_category_name("Non-Fiction")
        context["sciencefictions"] = self.get_books_by_category_name("Science-Fiction")
        return context
