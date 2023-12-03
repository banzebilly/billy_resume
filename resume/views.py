
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Thank you  your message has been sent!'
             # Redirect to the same page after form submission
    else:
        form = ContactForm()

    return render(request, 'paul_billy/index.html', {'form': form})


