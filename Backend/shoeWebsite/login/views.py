
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
from .forms import userRegistration
from django.views.decorators.cache import never_cache

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            user = form.get_user()
            login(request, user)
            
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('register')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
    
@never_cache
def register(request):
    if request.method == 'POST':
        form = userRegistration(request.POST)
        
        # 1. Add parentheses ()
        if form.is_valid(): 
            form.save()
            
            # 2. Add 'request' as the first argument
            messages.success(request, 'You have successfully registered!')
            
            # 3. Add 'return' keyword
            return redirect('/login') 

    else:
        form = userRegistration()

    return render(request, 'register.html', {'form': form})
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    
    # If someone tries to access it via URL directly, send them home
    return redirect('home')