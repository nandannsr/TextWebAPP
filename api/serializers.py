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


""" Serializer to include the links of snippets with the details """


class SnippetHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='snippets-detail')

    class Meta:
        model = Snippet
        fields = ['url', 'title', 'content', 'created_at']


""" Serializer to include the snippets with the selected Tag"""


class TagDetailSerializer(serializers.ModelSerializer):
    snippets = SnippetSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
