from django.conf import settings
import os
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from PIL import Image as PILImage

from .models import Image as UploadedImage
from .serializers import ImageSerializer


class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):

        file_serializer = ImageSerializer(data=request.data)

        if file_serializer.is_valid():
            instance = file_serializer.save()
            # Check if the original_image field has an associated file
            if not instance.original_image:
                return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

            original_image_path = instance.original_image.path
            image = PILImage.open(original_image_path)
            greyscale_image = image.convert('L')

            # Extract directory and filename from the original_image_path
            directory, filename = os.path.split(original_image_path)
            # Prefix the filename with "greyscale_"
            greyscale_filename = f"greyscale_{filename}"

            # Construct the new greyscale_image_path
            greyscale_image_path = os.path.join(settings.MEDIA_ROOT, 'greyscale_images', greyscale_filename)

            # Ensure the directory exists before saving the greyscale image
            os.makedirs(os.path.dirname(greyscale_image_path), exist_ok=True)

            greyscale_image.save(greyscale_image_path)
            instance.greyscale_image = os.path.relpath(greyscale_image_path, settings.MEDIA_ROOT)
            instance.save()
            print('DATA', file_serializer.data)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
