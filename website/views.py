from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import ContatoForm
from django.contrib.auth import logout
from django.contrib.auth.forms import *
import json
from django.views import View
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from chatterbot import ChatBot

# Create your views here.

def index(request):
    form = ContatoForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect("index")
    return render(request, 'website/index.html',{"form": form})

def logoutView(request):
    logout(request)
    return render(request, 'registration/logout.html')

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')
    
def password_reset_confirm(request):    
    return render(request, 'registration/password_reset_confirm.html')

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')

def password_reset_form(request):
    return render(request, 'registration/password_reset_form.html')

def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'website/cadastro.html', {'form': form})

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


# -------------------------------- CHATTERBOT -------------------------------------------------------------------
'''
class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })'''