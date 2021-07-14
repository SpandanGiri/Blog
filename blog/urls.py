"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView 
from .views import PostDetailView
from .views import PostCreateView
from .views import PostUpdateView
from .views import PostDeleteView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',PostListView.as_view(),name="blog"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="blog-detail"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name="blog-update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="blog-delete"),
    path('post/new/',PostCreateView.as_view(),name="blog-create"),
    path('about/',views.about,name="about"),
    path('user/', include('users.urls')),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
