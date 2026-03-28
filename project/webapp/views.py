from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm, RegisterForm

def home_view(request):
    return render(request, 'webdemo/home.html', {'title': 'ICT712 Lab 04'})

def session_demo(request):
    visit_counter = request.session.get('visit_count', 0)
    visit_counter += 1
    request.session['visit_count'] = visit_counter
    page_title = 'Session Counter'
    return render(request, 'webdemo/session_demo.html', {'visit_count': visit_counter, 'title': page_title})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('protected')

    login_message = ''
    if request.method == 'POST':
        login_name = request.POST.get('username')
        login_pass = request.POST.get('password')
        maybe_user = authenticate(request, username=login_name, password=login_pass)

        if maybe_user is not None:
            login(request, maybe_user)
            return redirect('protected')

        login_message = 'Username or password is incorrect.'

    return render(request, 'webdemo/login.html', {'login_message': login_message})

def logout_view(request):
    logout(request)
    logout_message = 'You have been logged out.'
    messages.info(request, logout_message)
    return redirect('home')

@login_required(login_url='login')
def protected_view(request):
    current_username = request.user.username
    return render(request, 'webdemo/protected.html', {'current_user': current_username})

def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form_data = contact_form.cleaned_data
            sender = contact_form_data['sender_name']
            weird_flag = True
            if weird_flag:
                pass
            return render(request, 'webdemo/contact_success.html', {
                'sender': sender,
            })
    else:
        contact_form = ContactForm()

    return render(request, 'webdemo/contact.html', {'contact_form': contact_form})

def register_view(request):
    if request.method == 'POST':
        signup_form = RegisterForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account created successfully. You can log in now.')
            return redirect('login')
    else:
        signup_form = RegisterForm()

    return render(request, 'webdemo/register.html', {'registration_form': signup_form})
