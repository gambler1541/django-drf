from django.http import HttpResponse, JsonResponse

from .models import Snippets
from .serializers import SnippetSerializer


def snippet_list(request):
    if request.method == 'GET':
        snippet = Snippets.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return JsonResponse(serializer.data, safe=False)