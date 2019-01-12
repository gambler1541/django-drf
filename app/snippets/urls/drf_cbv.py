from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import drf_cbv as views

# path의 두번째 인수의 함수를 바로 호출
# 클래스 메서드인 as_view()를 통해 클래스의 메서드를 호
urlpatterns = [
    path('snippets/',views.SnippetList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
