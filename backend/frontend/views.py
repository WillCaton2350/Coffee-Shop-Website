from django.shortcuts import render
from django.http import HttpResponse
from .form import ReviewForm


def home(request):
    return render(
        request,
        'home.html'
        )
def menu(request):
    return render(
        request,
        'menu.html'
        )
def about(request):
    return render(
        request,
        'about.html'
        )
def sponsers(request):
    return render(
        request,
        'sponsers.html'
        )
def careers(request):
    return render(
        request,
        'careers.html'
        )


def reviewForm(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully")
        else:
            return HttpResponse("Form is not valid")
    else:
        form = ReviewForm()
        return render(request, 'contact.html', {'form': form})
