from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
# Create your models here.

class user_profile (models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(default='images.png' , upload_to='profile_pics' , verbose_name='الصورة الشخصية')

    def save (self , *args , **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300 :
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self) :
        return '{} profile.'.format(self.user.username)
def create_profile (sender , **kwarg) :
    if kwarg['created'] :
      user_profile.objects.create(user=kwarg['instance'])
post_save.connect(create_profile ,sender=User)
