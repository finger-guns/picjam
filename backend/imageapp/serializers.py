from rest_framework import serializers
from .models import Image as UploadedImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('id', 'original_image', 'greyscale_image')
