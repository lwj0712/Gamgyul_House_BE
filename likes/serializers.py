from django.contrib.auth import get_user_model

from rest_framework import serializers

from accounts.serializers import SimpleUserSerializer
from .models import Like

User = get_user_model()


class LikeSerializer(serializers.ModelSerializer):
    """좋아요 모델의 serializer"""

    user = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ["id", "user", "post", "created_at"]
        read_only_fields = ["user", "post"]
