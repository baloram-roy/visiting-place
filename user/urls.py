from django.urls import path
from user.views import login_view, logout_view, profile_view,register_view

urlpatterns = [
    path('login/', login_view, name='user-login'),
    path('logout/', logout_view, name='user-logout'),
    path('register/', register_view, name='user-register'),
    path('profile/', profile_view, name='user-profile'),
]
