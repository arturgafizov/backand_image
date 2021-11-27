from rest_framework import serializers


class JWTTokenSerializer(serializers.Serializer):
    domain = serializers.CharField(max_length=128)
    extension = serializers.CharField(max_length=128)
    file_size = serializers.FloatField()


class ImageSerializer(serializers.Serializer):
    image1 = serializers.ListField(child=serializers.ImageField(), required=False)
