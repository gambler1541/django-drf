from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Snippets
from ..serializers import SnippetSerializer

# APIView를 상속받음
class SnippetList(APIView):
    def get(self, request, format=None):
        snippet = Snippets.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippets.objects.get(pk=pk)
        except Snippets.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None, **kwargs):
        # kwargs = dict
        # kwargs[''] = 값을 참조
        # kwargs.get('partial', False) : defautl를 False
        # kwargs.pop은 get과 동일하나 인자에서 빼버림
        partial = kwargs.pop('partial', False)
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        return self.put(request, pk, format, partial=True)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

