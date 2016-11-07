from rest_framework import viewsets
from Comments.models import Comment
from Comments.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all comments to be created, or viewed.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PopQuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Pop Quiz comments to be created, or viewed.
    """
    queryset = Comment.objects.filter(content_url__contains='pop-quiz')
    serializer_class = CommentSerializer
    

class PlanetaryMotionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Planetary Motion comments to be created, or viewed.
    """
    queryset = Comment.objects.filter(content_url__contains='planetary-motion')
    serializer_class = CommentSerializer

class LowAltitudeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Low Altitude Launch comments to be created, or viewed.
    """
    queryset = Comment.objects.filter(content_url__contains='low-altitude-launch')
    serializer_class = CommentSerializer

