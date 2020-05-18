from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from custom_user.forms import LoginForm, SignupForm
from custom_user.models import MyCustomUser
from customUser.settings import AUTH_USER_MODEL

# Create your views here.


@login_required
def homepage_view(request):
    if not request.user.display_name:
        display_name = 'None on file'
    else:
        display_name = request.user.display_name

    return render(
        request,
        'index.html',
        {
            'username': request.user.username,
            'display_name': display_name,
            'model_location': AUTH_USER_MODEL
        })


def signup_view(request):
    # POST request handling
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            new_user = MyCustomUser.objects.create_user(
                username=form_data['username'],
                password=form_data['password'],
                display_name=form_data['display_name'],
                homepage=form_data['homepage'],
                age=form_data['age']
            )
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))

    # GET request handling
    form = SignupForm()
    return render(
        request,
        'form.html',
        {
            'title': 'Sign Up',
            'button_value': 'Create User',
            'form': form
        }
    )


def login_view(request):
    # POST request handling
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_creds = form.cleaned_data
            user = authenticate(
                request,
                username=user_creds['username'],
                password=user_creds['password'])

            if user:
                login(request, user)
                if request.GET.get('next'):
                    redirect_path = request.GET['next']
                    return HttpResponseRedirect(redirect_path)
                return HttpResponseRedirect(reverse('home'))

    # GET request handling
    form = LoginForm()
    return render(
        request,
        'form.html',
        {
            'title': 'Log In',
            'button_value': 'Log In',
            'form': form,
            'message': True
        }
    )


def logout_view(request):
    logout(request)
    return (HttpResponseRedirect(reverse('home')))
