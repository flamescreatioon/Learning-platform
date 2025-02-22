from rest_framework import generics, permissions
from .models import Course, LectureMaterial
from .serializers import CourseSerializer, LectureMaterialSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(lecturer=self.request.user)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class LectureMaterialListCreateView(generics.ListCreateAPIView):
    queryset = LectureMaterial.objects.all()
    serializer_class = LectureMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class LectureMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LectureMaterial.objects.all()
    serializer_class = LectureMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    
