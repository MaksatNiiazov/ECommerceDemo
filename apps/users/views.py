from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from .models import CustomUser, Address
from .forms import UserRegistrationForm, UserProfileForm, AddressForm

class UserRegistrationView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('profile_template')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile_template')

    def get_object(self):
        return self.request.user

class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'users/address_form.html'
    success_url = reverse_lazy('address_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'users/address_form.html'
    success_url = reverse_lazy('address_list')

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'users/address_confirm_delete.html'
    success_url = reverse_lazy('address_list')

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LoginView(AuthLoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')

class LogoutView(AuthLogoutView):
    next_page = reverse_lazy('login')  # Перенаправление на страницу логина после выхода
