from django.contrib.gis.geoip2 import GeoIP2
import socket


def get_client_ip(request):
    """Get client IP address from request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_user_agent(request):
    """Get user agent from request."""
    return request.META.get('HTTP_USER_AGENT', '')


def get_referrer(request):
    """Get referrer from request."""
    return request.META.get('HTTP_REFERER', None)


def validate_affiliate_url(url):
    """Validate if URL is reachable."""
    try:
        socket.create_connection((socket.gethostbyname(socket.gethostname()), 80), timeout=5)
        return True
    except (socket.timeout, socket.error):
        return False
