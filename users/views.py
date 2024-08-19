from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserForm 
from django.contrib.auth import logout
from django.views import View

class LoginUser(LoginView):
    template_name = "users/login_user.html"
    form_class = AuthenticationForm
    extra_context = {"title": "Login"}

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = reverse_lazy('shop:home')
        return next_url


class LogoutUser(View):
    def post(self, request):
        logout(request)
        return redirect('shop:home')

    def get(self, request):
        return redirect('shop:home') 


class RegisterUser(CreateView):
    template_name = "users/register_user.html"
    form_class = CustomUserForm
    extra_context = {"title": "Register"}
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        return redirect(self.success_url)


    







    

