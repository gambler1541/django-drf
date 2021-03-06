from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

from .models import (
    LANGUAGE_CHOICES,
    STYLE_CHOICES,
    Snippets,
)
#
# class SnippetsSerializer(serializers.Serializer):
#     # 역직렬화 할때에는 사용하지 않음(read_only=True)
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         return Snippets.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
#

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = (
            'pk',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'snippets_set',

        )