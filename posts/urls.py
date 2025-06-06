from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("<int:pk>/detail", views.PostDetailView.as_view(), name="detail"),
]