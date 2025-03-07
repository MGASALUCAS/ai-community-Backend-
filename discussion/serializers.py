from rest_framework import serializers
from .models import Discussion, DiscussionComment, DiscussionLike

class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'

class DiscussionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionComment
        fields = '__all__'

class DiscussionLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionLike
        fields = '__all__'
