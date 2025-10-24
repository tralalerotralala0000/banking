from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path("", views.index, name="index"),
    path('countries/', views.country_list, name='country_list'),
    path('countries/<int:pk>/edit/', views.country_edit, name='country_edit'),
]