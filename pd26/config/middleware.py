# Zadania 7
class SimpleRequestCatcherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        method = request.method
        print(f"Used request with method: {method}")
        response = self.get_response(request)
        return response
    
# Zadanie 13
class IPLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(f"IP użytkownika: {ip} | Path: {request.path}")
        response = self.get_response(request)
        return response
    
# Zadanie 14
from django.http import JsonResponse

class IPBlockerMiddleware:
    blocked_ips = ['127.0.0.1'] 
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.blocked_ips:
            return JsonResponse({'error' : 'Adres IP zabkolowany'}, status=403)
        response = self.get_response(request)
        return response