from django.urls import path
from .views import home, nepal

urlpatterns = [
    path('', home, name='home'),
    path('nepal/', nepal, name='nepal'),
]
