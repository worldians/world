from django.urls import path
from .views import (
    PostDeleteView,
    PostListview,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('', PostListview.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
