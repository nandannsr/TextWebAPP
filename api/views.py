from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tag, Snippet
from drf_spectacular.utils import extend_schema
from .serializers import TagSerializer, SnippetSerializer, TagDetailSerializer

# Create your views here.

""" View for getting the count of the snippets as well as the Snippet List"""


class OverviewAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=SnippetSerializer)
    def get(self, request):
        snippet_count = Snippet.objects.count()
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True, context={'request': request})
        snippet_list = serializer.data

        response_data = {
            'snippet_count': snippet_count,
            'snippets': snippet_list
        }

        return Response(response_data)


""" View for listing the snippets as well as creating a new snippet """


class SnippetListView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        tag_title = self.request.data.get('tag')
        if tag_title:
            tag, _ = Tag.objects.get_or_create(title=tag_title)
            serializer.save(user=self.request.user, tag=tag)
        else:
            serializer.save(user=self.request.user)


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
