from django.urls import path

from ..views import drf_fbv as views

urlpatterns = [
    path('snippets/', views.snippet_list),

]