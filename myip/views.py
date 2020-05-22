from django.shortcuts import render

def myip(request): 
    context = { 
                    'myip' : request.META.get("REMOTE_ADDR"),
                    'myhost' : request.META.get("REMOTE_HOST"),
                    'forwarded_for' : request.META.get("X_FORWARDED_FOR"),
              }

    return render(request, 'myip.html', context)

