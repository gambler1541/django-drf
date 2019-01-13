from django.urls import path, include

from . import django_fbv, drf_fbv, drf_cbv, drf_mixin, drf_generic_cbv

urlpatterns = [
    path('django-fbv/', include(django_fbv)),
    path('drf-fbv/', include(drf_fbv)),
    path('drf-cbv/', include(drf_cbv)),
    path('drf-mixins/', include(drf_mixin)),
    path('drf-generic-cbv/', include(drf_generic_cbv)),

]