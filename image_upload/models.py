from django.db import models
# Create your models here.

class ImageUploader(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length = 100 , default = '')
   
    def __str__(self):
        return self.display_name