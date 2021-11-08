from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_function):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_function(request, *args, **kwargs)
        else:
            print(request.user)
            return redirect('login')

    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(f'You user: {request.user} are not allowed on this site')

        return wrapper_func
    return decorator