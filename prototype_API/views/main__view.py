from django.shortcuts import render


# common view, main view
def home(request):
    return render(request, 'home.html')
