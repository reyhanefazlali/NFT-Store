from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/account/logged/')

    forms = AuthenticationForm()
    return render(request, 'account/login.html', {'forms': forms})


def logged(request):
    return render(request, 'account/redirect.html')


def signup_views(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = UserCreationForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('/account/signedup/')

    forms = UserCreationForm()
    return render(request, 'account/signup.html')


def signedup(request):
    return render(request, 'account/redirect-signup.html')


@login_required
def logout_views(request):
    logout(request)
    return render(request, 'account/redirect-logout.html')
