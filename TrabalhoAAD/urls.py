from django.contrib import admin
from django.urls import path
from TrabalhoAAD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('home_next/', views.home_next,name="home_next")
]
