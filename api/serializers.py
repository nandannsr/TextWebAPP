from rest_framework import serializers
from .models import Tag, Snippet


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializer(required=False)

    class Meta:
        model = Snippet
        fields = ['title', 'content', 'tag', 'created_at']



