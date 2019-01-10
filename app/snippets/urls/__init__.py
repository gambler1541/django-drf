from django.urls import path, include

from . import django_fbv, drf_fbv

urlpatterns = [
    path('django-fbv/', include(django_fbv)),
    path('drf-fbv/', include((drf_fbv))),

]