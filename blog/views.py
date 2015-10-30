from django.shortcuts import render
from django.contrib.auth import authenticate, login

def post_list(request):
    email = request.user.email
    return render(request, 'blog/post_list.html', {'email':email})

def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return render(request, 'blog/post_list.html', {})
            else:
                pass
                # Return a 'disabled account' error message

        else:
            # Return an 'invalid login' error message.
            pass
    else:
        return render(request, 'login.html', {})

def post(request):
    if request.user.is_authenticated() :

        if request.method == "POST":
            
            pass
        else:
            pass
    else:
        pass
