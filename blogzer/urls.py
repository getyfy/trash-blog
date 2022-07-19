"""blogzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import register_request, login_request, logout_request, password_reset_request
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("articles", include("blog.urls")),
    path('register', register_request, name="register"),
    path('login', login_request, name="login"),
    path('logout', logout_request, name="logout"),
    path('password-reset/', password_reset_request, name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="blog/registration/password_reset_done.html"), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="blog/registration/password_reset_confirme.html"), name="password_reset_confirm"),
    path('password-reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="blog/registration/password_reset_complete.html"), name="password_reset_complete"),
    
    
]
