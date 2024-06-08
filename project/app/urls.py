from django.urls import path
from .views import *

urlpatterns = [
    path('',Insert,name='Insert'),
    path('Show/',Show,name='Show'),
    path('Editpage/<int:pk>',Editpage,name='Editpage'),
    path('Update/<int:pk>',Update,name='Update'),
    path('Delete/<int:pk>',Delete,name='Delete'),
]
