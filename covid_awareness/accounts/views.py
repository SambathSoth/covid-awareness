from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            user.save()
            return redirect('hospital:index')
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')