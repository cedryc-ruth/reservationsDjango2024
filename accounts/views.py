from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserSignUpForm
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login

class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("accounts:user-profile")
    template_name = "user/update.html"

    def test_func(self):
        pkInURL = self.kwargs['pk']
        return self.request.user.is_authenticated and self.request.user.id==pkInURL or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Vous n'avez pas l'autorisation d'accéder à cette page!")
        return redirect('accounts:user-profile')

class UserSignUpView(UserPassesTestMixin, CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def test_func(self):
        return self.request.user.is_anonymous or self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, "Vous êtes déjà inscrit!")
        return redirect('home')

@login_required
def profile(request):
    languages = {
        "fr": "Français",
        "en": "English",
        "nl": "Nederlands",
    }

    return render(request, 'user/profile.html', {
        "user_language" : languages[request.user.usermeta.langue],
    })

@login_required
def update(request, user_id):
    user = User.objects.get(id=request.user.id)
    userForm = UserUpdateForm(request.POST or None, instance=user)

    if userForm.is_valid():
        userForm.save()

        login(request, user)
        messages.success(request, 'Modification réussie.')
        return redirect('home')
    return render(request, 'user/update.html', {'userForm':userForm})