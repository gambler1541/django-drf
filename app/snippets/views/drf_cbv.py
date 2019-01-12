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