from django.shortcuts import render, resolve_url, redirect
from chat_app.settings import NOT_LOGIN_REDIRECT_URL

def user_not_authenticated(function=None, login_url=None, redirect_url=NOT_LOGIN_REDIRECT_URL):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return function(request, *args, **kwargs)

        return redirect(redirect_url)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
