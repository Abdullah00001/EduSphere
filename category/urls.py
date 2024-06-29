from django.urls import path, include
from category.views import CategoriesBookView

urlpatterns = [
    path("categories-books/<str:category_name>/", CategoriesBookView, name="books_by_category"),
]
