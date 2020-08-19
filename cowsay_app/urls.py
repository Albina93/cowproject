from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('recent/', views.recent, name="recent")
]
