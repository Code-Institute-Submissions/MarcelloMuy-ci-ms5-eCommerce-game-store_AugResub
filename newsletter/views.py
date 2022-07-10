"""Imported"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm


def newsletter(request):
    """A view to handle newsletter signup"""

    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            messages.error(
                request,
                f"Sorry, {instance.email} already exists in our database.\
                           Please check and try again.",
            )
            return redirect("home")
        else:
            instance.save()
            messages.success(
                request,
                f"Congratulations! {instance.email} \
                has been added to our mailing list",
            )
            return redirect("home")

    template = "home/index.html"
    context = {
        "form": form,
    }
    return render(request, template, context)
