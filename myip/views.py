from django.shortcuts import render

def myip(request): 
    context = { 
                    'myip' : request.META.get("REMOTE_ADDR"),
                    'myhost' : request.META.get("REMOTE_HOST"),
              }

    return render(request, 'myip.html', context)

