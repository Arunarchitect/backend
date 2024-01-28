from rest_framework import generics, permissions
from django.db.models import Q
from .models import Tag, Blog
from .serializers import TagSerializer, BlogSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class BlogListCreateView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Blog.objects.all()
        tagname = self.request.query_params.get('tagname', None)

        if tagname:
            # Assuming tags is now a CharField, use Q objects for case-insensitive search
            queryset = queryset.filter(Q(tags__icontains=tagname))

        return queryset

    def get_serializer_class(self):
        return BlogSerializer

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
