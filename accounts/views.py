from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

#from .forms import SignUpForm

class SignUpView(UserPassesTestMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    permission_denied_message = "Vous êtes déjà inscrit!"

    def test_func(self):
        return self.request.user.is_anonymous or self.request.user.is_superuser
    
    def handle_no_permission(self):
        return redirect('home')