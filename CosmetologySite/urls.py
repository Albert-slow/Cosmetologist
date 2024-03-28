"""
URL configuration for CosmetologySite project.

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
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from procedures import views
from procedures.views import HomePage, MyLoginView, logout_view, search, category_page, procedure_page, posts_page, post_list, contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('category/<int:pk>', category_page),
    path('procedure/<int:pk>', procedure_page),
    path('post/<int:pk>', posts_page),
    path('posts/', post_list),
    path('login/', MyLoginView.as_view()),
    path('logout/', logout_view),
    path('search', search),
    path('contact/', contact_us, name='contact')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

