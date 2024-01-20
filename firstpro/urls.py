from django.urls import path
from firstpro.views import index

urlpatterns = [
    path('', index, name='index')
]
