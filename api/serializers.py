from rest_framework import serializers
from .models import Tag, Snippet


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


""" Snippet Serializer to include the Links also """


class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializer(required=False)
    url = serializers.HyperlinkedIdentityField(read_only=True, required=False, view_name='snippets-detail')

    class Meta:
        model = Snippet
        fields = ['url', 'title', 'content', 'tag', 'created_at']


""" Serializer to include the snippets with the selected Tag"""


class TagDetailSerializer(serializers.ModelSerializer):
    snippets = SnippetSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
