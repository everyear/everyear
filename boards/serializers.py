from boards.models import Content, Comment
from rest_framework  import serializers

class contentSerializer(serializers.Serializer):
    class Meta:
        model = Content
        fields = '__all__'
    


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = '__all__'


