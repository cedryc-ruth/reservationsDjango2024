from django.urls import path
from .views import SignUpView
from .views import profile
from .views import edit

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='user-profile'),
    path('profile/<int:user_id>', edit, name='user-edit'),
]