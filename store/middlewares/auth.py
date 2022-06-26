from django.shortcuts import render, redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if not request.session.get('cutomer'):
            return redirect('login')

        response = get_response(request)

 
        return response

    return middleware