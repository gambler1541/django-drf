from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from ..models import Snippets
from ..serializers import SnippetSerializer

@api_view(['GET','POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet = Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method in ('PATCH','PUT'):
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(
            snippet, data=data,
            # PATCH면 True
            # PUT이면 False
            partial= (request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



