from rest_framework import serializers

from .models import Article


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=120)
#     description = serializers.CharField()
#     body = serializers.CharField()
#     author_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.author_id = validated_data.get('author_id', instance.author_id)
#
#         instance.save()
#         return instance


# Our serializer, however, is replicating a lot of information that’s also contained in the Article model.
# I think it would be nice if we could keep our code a bit more concise.
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'description',
            'body',
            'author_id'
        )
