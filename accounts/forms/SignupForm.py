from django import forms
from  django.contrib.auth.forms import UserCreationForm
from  catalogue.models import UserMeta

class SignUpForm(UserCreationForm):
    pass
    '''
    class Meta:
        model = UserMeta

        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'langue',
        ]
'''