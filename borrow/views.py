from django.shortcuts import render, redirect
from book.models import BookModel
from borrow.models import BookBorrowModel, BookReturnModel
from account.models import ProfileModel

# Create your views here.
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


def order_email(user, amount, book, subject):
    message = render_to_string(
        "borrow/order_email.html",
        {
            "user": user,
            "book": book,
            "amount": amount,
            "operation": subject,
        },
    )
    to_email = [user.email]
    if isinstance(message, tuple):
        message = "".join(message)
    send_email = EmailMultiAlternatives(subject=subject, body="", to=to_email)
    send_email.attach_alternative(message, "text/html")
    send_email.send()


def borrowView(request, id):
    requested_book = BookModel.objects.get(id=id)
    requested_book.book_quantity -= 1
    requested_book.save()
    requested_user = ProfileModel.objects.get(user=request.user)
    requested_user.balance -= requested_book.book_price
    order_email(
        request.user, requested_book.book_price, requested_book.book_name, "Borrow"
    )
    requested_user.save()
    borrowObject = BookBorrowModel.objects.create(
        user=request.user,
        book=requested_book,
        status=True,
    )
    borrowObject.save()
    return redirect("car_detail", pk=id)


def returnView(request, id):
    requested_book = BookModel.objects.get(id=id)
    requested_book.book_quantity += 1
    requested_book.save()
    requested_user = ProfileModel.objects.get(user=request.user)
    requested_user.balance += requested_book.book_price
    order_email(
        request.user, requested_book.book_price, requested_book.book_name, "Return"
    )
    requested_user.save()
    returnObject = BookReturnModel.objects.create(
        user=request.user,
        book=requested_book,
        status=True,
    )
    borrow_status = BookBorrowModel.objects.get(
        book=requested_book, user=request.user, status=True
    )
    borrow_status.status = False
    borrow_status.save()

    returnObject.save()

    return redirect("car_detail", pk=id)
