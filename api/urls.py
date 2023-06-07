from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippets-detail'),
    path('tags/', TagListView.as_view()),
    path('tags/<int:pk>/', TagDetailView.as_view()),

]
