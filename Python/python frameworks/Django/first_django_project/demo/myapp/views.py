from django.shortcuts import render, HttpResponse  # noqa: F401

# Create your views here.
def home (request):
    return render(request, 'home.html')
