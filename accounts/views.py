from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserAdminCreationForm

# Create your views here.

class RegisterView(LoginRequiredMixin,CreateView):
    model = User
    template_name = 'accounts/registro.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('dashboard:dashboard')
vwRegister = RegisterView.as_view()