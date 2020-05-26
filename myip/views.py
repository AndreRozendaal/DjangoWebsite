from django.shortcuts import render

def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        my_ip = x_forwarded_for.split(',')[0]
        my_ip = my_ip.split(':')[0]
    else:
        my_ip = request.META.get('REMOTE_ADDR')
    return my_ip

def myip(request):
    context = {'myip' : visitor_ip_address(request)}

    return render(request, 'myip.html', context)
