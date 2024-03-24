from .forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import User



class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('my_account_page')


class Login(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('my_account_page')

    def get_success_url(self):
        return self.success_url


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('login_page')


class Account(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'account.html'
    fields = ['username', 'email', 'first_name', 'last_name', 'photo']  
    success_url = reverse_lazy('my_account_page')  

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        if 'photo' in self.request.FILES:
            self.object.photo = self.request.FILES['photo']
        return super().form_valid(form)

    
    