from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    # Sprawdzamy, czy metoda żądania to POST (wysyłka formularza)
    if request.method == 'POST':
        # Tworzymy instancję formularza z danymi z żądania
        form = UserCreationForm(request.POST)
        # Sprawdzamy, czy formularz jest poprawny
        if form.is_valid():
            form.save() # Zapisujemy użytkownika w bazie danych
            username = form.cleaned_data.get('username')
            # Wyświetlamy komunikat o sukcesie
            messages.success(request, f'Konto dla {username} zostało utworzone! Możesz się teraz zalogować.')
            return redirect('login') # Przekierowujemy na stronę logowania
    else:
        # Jeśli metoda to GET, tworzymy pusty formularz
        form = UserCreationForm()
    # Renderujemy szablon z formularzem
    return render(request, 'users/register.html', {'form': form})

# Zadanie 3 - strona profilu
@login_required
def profile(request):
    return render(request, 'users/profile.html')

# Zadanie 5 - strona główna tylko dla zalogowanych
@login_required
def home(request):
    return render(request, 'home.html')

# def logout(request):
#     request.session.flush()
#     return render(request, 'users/logout.html')