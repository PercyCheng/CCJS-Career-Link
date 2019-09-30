from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

@login_required
def accountView(request):
    return render(request, 'account.html')

def registerView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form':form})
