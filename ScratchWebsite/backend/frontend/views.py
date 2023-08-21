from django.shortcuts import render
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
            return render(request,'home.html')
    else:
        form = ReviewForm()
        return render(request, 'contact.html', {'form': form})