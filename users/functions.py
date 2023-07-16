from functools import wraps
from django.http import Http404

def allow_access_to_superuser(func):
    """
    Decorator to allow access to superuser only.

    This decorator checks if the user is authenticated and is a superuser.
    If the user is authenticated and is a superuser, the decorated view function is called.
    Otherwise, a Http404 exception is raised.
    """
    @wraps(func)
    def inner(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            raise Http404

        return func(request, *args, **kwargs)

    return inner
