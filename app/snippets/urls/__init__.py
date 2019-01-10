from django.urls import path
from ..views import django_fbv

urlpatterns = [
    path('snippets/', django_fbv.snippet_list),
    path('snippets/<int:pk>/', django_fbv.snippet_detail),

]