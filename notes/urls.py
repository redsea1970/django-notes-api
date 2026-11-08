from django.urls import path
from .views import NoteListCreateView, NoteDetailView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("notes/", NoteListCreateView.as_view(), name="note-list"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
]
