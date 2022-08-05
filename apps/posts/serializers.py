from rest_framework import serializers

from apps.posts.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"
        read_only_fields = (
            'id',
            'user'
        )


class PostSerializer(serializers.ModelSerializer):
    post_image = PostImageSerializer

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = (
            'id',
            'create_at',
            'user'
        )
