from Comments.models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'comment', 'content_url', 'created', 'ip_address', 'username')
