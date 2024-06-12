from django.urls import path
from .views import client_list, client_detail


urlpatterns = [
    path('clients/', client_list, name='client-list'),
    path('clients/<int:pk>/', client_detail, name='client-detail'),
]

