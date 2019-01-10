from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from ..models import Snippets
from ..serializers import SnippetSerializer


__all__ = (
    'snippet_list',
    'snippet_detail',
)

# CSRF검증에서 제외되는 view
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippet = Snippets.objects.all()
        # Snippets QuerySet을 생성자로 사용한 SnippetSerializer 인스턴스
        serializer = SnippetSerializer(snippet, many=True)
        # JSON형식의 문자열을 HttpResponse로 돌려줌 (content_type에 'application/json'명시됨)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # request를 분석해서 전달받은 JSON형식 문자열을 파이썬 데이터형으로 파싱
        data = JSONParser().parse(request)
        # data인수를 채우면서 Serializer인스턴스 생성 (역직렬화 과정)
        serializer = SnippetSerializer(data=data)
        # Seiralizer의 validation
        if serializer.is_valid():
            # valid한 경우, Serializer의 save()메서드로 새 Snippet인스턴스 생
            serializer.save()
            # 생성 후 serializer.data로 직렬화한 데이터를 JSON방식으로 리턴하며 201(created)상태코드 전달
            return JsonResponse(serializer.data, status=201)
        # invalid한 경우, error목록을 JSON형식으로 리턴하며 400(Bad request)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



    elif request.method == 'DELETE':
        snippet.delete()
        # 204는 성공했지만 보여줄 content는 없음(No content)
        return HttpResponse(status=204)