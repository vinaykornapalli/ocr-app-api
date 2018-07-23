from rest_framework import serializers
from .models import ImageUploader


class ImageUploadSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(upload_to='images/%Y/%m/%d')
    # created = serializers.DateTimeField(auto_now_add=True)
    # display_name = serializers.CharField(max_length = 100 , default = '')
    
    class Meta:
        model = ImageUploader
        fields = ('display_name' , 'image' , 'created')
    # def create(self , **data):
    #     return ImageUploader.objects.create(**data)
   
