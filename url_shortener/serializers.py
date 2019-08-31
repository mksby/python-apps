from rest_framework import serializers

from .models import URL


class UrlSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=120)
    short = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return URL.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('url', instance.url)
        instance.description = validated_data.get('short', instance.short)
        instance.save()
        return instance