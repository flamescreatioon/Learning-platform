from django.urls import path
from .views import (CourseListCreateView, CourseDetailView, LectureMaterialListCreateView, LectureMaterialDetailView)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('materials/', LectureMaterialListCreateView.as_view(), name='material-list-create'),
    path('materials/<int:pk>/', LectureMaterialDetailView.as_view(), name='material-detail'),
]