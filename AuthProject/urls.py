
from django.contrib import admin
from django.urls import path , include
from AuthProject.core import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home , name="home"),
    path('signup/' , views.signup,name="signup" ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
