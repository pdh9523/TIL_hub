from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserListSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserListSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = (
            'id', 'content', 'author', 'author_id',
            'article', 'created_at', 'updated_at'
        )
        read_only_fields = ('article', 'created_at', 'updated_at')


class ArticleListSerializer(serializers.ModelSerializer):
    author = UserListSerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'author',
            'comment_count', 'created_at'
        )

    def get_comment_count(self, obj):
        return obj.comments.count()


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = UserListSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'content', 'author',
            'comments', 'comment_count',
            'created_at', 'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at')

    def get_comment_count(self, obj):
        return obj.comments.count()


class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)