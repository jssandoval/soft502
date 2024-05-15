from django.urls import path
from django.contrib.auth import views as auth_views

from core.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html'), name='login')
]
