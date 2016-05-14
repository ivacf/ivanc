from rest_framework import serializers
from rest_api.models import App, Repo, Article


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = ('id', 'title', 'url', 'store_url', 'start_date', 'end_date', 'image',
                  'color', 'platform',)
        read_only_fields = ('image',)


class AppSerializerNested(AppSerializer):
    """
    Extension of AppSerializer that enables one level of nested objects.
    """
    class Meta(AppSerializer.Meta):
        # Extends Meta of AppSerializer, hence will use same model and fields
        depth = 1


class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repo
        fields = ('id', 'title', 'subtitle', 'url', 'start_date', 'end_date', 'image', 'color',
                  'platform',)
        read_only_fields = ('image',)


class RepoSerializerNested(RepoSerializer):
    """
    Extension of RepoSerializer that enables one level of nested objects.
    """
    class Meta(RepoSerializer.Meta):
        # Extends Meta of AppSerializer, hence will use same model and fields
        depth = 1


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'publish_date', 'image', 'color',
                  'platform',)
        read_only_fields = ('image',)


class ArticleSerializerNested(ArticleSerializer):
    """
    Extension of ArticleSerializer that enables one level of nested objects.
    """
    class Meta(ArticleSerializer.Meta):
        # Extends Meta of AppSerializer, hence will use same model and fields
        depth = 1
