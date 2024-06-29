from django.urls import path, include
from core.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("account/", include("account.urls")),
    path("book/", include("book.urls")),
    path("borrow/", include("borrow.urls")),
    path("category/", include("category.urls")),
    path("review/", include("review.urls")),
    path("transaction/", include("transaction.urls")),
]
