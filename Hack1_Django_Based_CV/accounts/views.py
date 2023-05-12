from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView, DetailView
from accounts.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import UserProfile


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

   
class AccountLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(AccountLoginView, self).form_valid(form)
        

    def get_success_url(self):
        user = self.request.user
        profile = user.profile
        return reverse('accounts:profile', args=[profile.id])

class ProfileView(DetailView):
    
    model = UserProfile
    template_name = 'accounts/profile.html'

class LogoutView(View):
   pass