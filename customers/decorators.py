from django.shortcuts import redirect
from django.http import HttpResponse


def unauthorized_user(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return view(request, *args, **kwargs)

    return wrapper


def allowed_role(allowed_user=[]):
    def function(view):
        def wrapper(request, *args, **kwargs):
            user_role = request.user.groups.all()[0].name
            role = user_role
            if role in allowed_user:
                return view(request, *args, **kwargs)
            else:
                return HttpResponse('You don`t have credentials to view this page')

        return wrapper

    return function


def strong_perm(view):
    def wrapper(request, *args, **kwargs):
        group = request.user.groups.all().first().name
        if group == 'admin':
            return view(request, *args, **kwargs)
        if group == 'customer':
            return redirect('user_page')

    return wrapper
