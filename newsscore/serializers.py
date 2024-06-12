
from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    image_url = serializers.URLField()
    article_url = serializers.URLField()
    sentiment = serializers.FloatField()
    senti_image = serializers.CharField()
