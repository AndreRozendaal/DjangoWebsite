from django.shortcuts import render

def homepage(request): 
   return render(request, 'homepage.html', {})

def error_404(request, exception):
   return render(request, 'homepage.html', {})
