from django.shortcuts import render

def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def myip(request): 
    context = { 
                    'myip' : visitor_ip_address(request),
              }

    return render(request, 'myip.html', context)

