from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tag, Snippet
from .serializers import TagSerializer, SnippetSerializer, TagDetailSerializer

# Create your views here.


""" View for getting a Particular Snippet for updating or deleting """


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]


""" View for getting the Tag list """


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


""" View for getting a particular Tag Detail """


class TagDetailView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    permission_classes = [IsAuthenticated]
