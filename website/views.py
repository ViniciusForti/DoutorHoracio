from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Contato
from .forms import ContatoForm

# Create your views here.

def index(request):
    form = ContatoForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect("index")
    return render(request, 'website/index.html',{"form": form})

@login_required
def usuario(request):
    return render(request, 'website/usuario.html',{})