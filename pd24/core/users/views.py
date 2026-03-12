from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm # Zadanie 6
from django.contrib import messages
from django.contrib.auth import login # Zadanie 9
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required # Zadanie 10
from django.contrib.auth.models import User # Zadanie 10

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            # Zadanie 9 - automatyczne logowanie po rejestracji
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Witaj {username}, Twoje konto zostało utworzone i jesteś teraz zalogowany.')
            return redirect('home')  # Przekierowujemy na stronę główną
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Zadanie 3
@login_required
def profile(request):
    return render(request, 'users/profile.html')

# Zadanie 5
@login_required 
def home(request):
    return render(request, 'users/home.html')

# Zadanie 10
@staff_member_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

