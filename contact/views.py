from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was saved. Thank you for contacting me.")
            return redirect("contact")
        messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})
