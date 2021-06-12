from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Contato
from .forms import ContatoForm
from django.contrib.auth.forms import *

# Create your views here.

def index(request):
    form = ContatoForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect("index")
    return render(request, 'website/index.html',{"form": form})

def logout(request):
    logout(request)
    return redirect('index')

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')
    
def password_reset_confirm(request):    
    return render(request, 'registration/password_reset_confirm.html')

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')

def password_reset_form(request):
    return render(request, 'registration/password_reset_form.html')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_contato.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

@login_required
def usuario(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)

    return render(request, 'website/usuario.html',{'form_senha': form_senha})