from django.shortcuts import render
from django.urls import reverse_lazy
from transaction.models import TransactionModel
from django.contrib import messages
from transaction.constants import DEPOSITE, WITHDRAW
from account.models import ProfileModel
from django.views.generic.edit import FormView
from transaction.forms import TransactionForm

# Create your views here.

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


def transaction_email(user, amount, subject):
    message = render_to_string(
        "transaction/transaction_mail.html",
        {
            "user": user,
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


class Transaction(FormView):
    form_class = TransactionForm
    transaction_type = None
    extra_context = None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = TransactionModel(transaction_type=self.transaction_type)
        return kwargs

    def form_valid(self, form):
        amount = form.cleaned_data["transaction_amount"]
        print(amount)
        requested_user = ProfileModel.objects.get(user=self.request.user)
        if self.transaction_type == DEPOSITE:
            requested_user.balance += amount
            transaction_email(self.request.user,amount,DEPOSITE)
            requested_user.save()
        elif self.transaction_type == WITHDRAW:
            if requested_user.balance >= amount:
                requested_user.balance -= amount
                transaction_email(self.request.user,amount,WITHDRAW)
                requested_user.save()
        TransactionModel.objects.create(
            user=self.request.user,
            transaction_amount=amount,
            transaction_type=self.transaction_type,
            after_transaction_balance=requested_user.balance,
        )
        
        return super().form_valid(form)


class DepositePageView(Transaction):
    template_name = "transaction/deposite.html"
    transaction_type = DEPOSITE

    def get_success_url(self):
        
        return reverse_lazy("profile", kwargs={"profilenav": "account"})
    


class WithdrawPageView(Transaction):
    template_name = "transaction/withdraw.html"
    transaction_type = WITHDRAW

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"profilenav": "account"})
    
    
