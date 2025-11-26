from django.shortcuts import redirect

def auth(view_function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated == 'False':
            return redirect('login')
        return (request, *args, *kwargs)
    return wrapper