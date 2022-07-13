"""dotolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from accounts.views import UserRegistrationView
from django.contrib.auth import views as auth_views
from lists.views import homeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homeView, name='home'),
    path('admin/', admin.site.urls),
    path('new-user/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', auth_views.LoginView.as_view() , name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home') , name='logout'),
    path('lists/', include('lists.urls') ,name= 'list'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)