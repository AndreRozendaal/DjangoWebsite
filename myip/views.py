from django.shortcuts import render

def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        my_ip = x_forwarded_for.split(',')[0]
        my_ip = my_ip.split(':')[0]
    else:
        my_ip = request.META.get('REMOTE_ADDR')
    return my_ip

def visitor_hostname(ip): 
    import socket
    try: 
        hname, aliases, ipaddrs = socket.gethostbyaddr(ip)
    except socket.error: 
        hname = "Uknown"
    return hname

def myip(request):
    ip = visitor_ip_address(request)
    context = {'myip' : ip, 'hostname' : visitor_hostname(ip)}

    return render(request, 'myip.html', context)
