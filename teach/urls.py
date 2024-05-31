"""
URL configuration for teach project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from elements.views import index, elements, test_context, first_lesson, second_lesson, third_lesson

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('elements/', elements, name='elements'),
    path('first-lesson/', first_lesson, name='first_lesson'),
    path('second-lesson/', second_lesson, name='second_lesson'),
    path('third-lesson/', third_lesson, name='third_lesson'),
    path('test_context/', test_context,name='test_context'),
    path('users/', include('users.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Глобальный путь для logout
    path('', include('django.contrib.auth.urls')),  # Для включения стандартных URL аутентификации
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
