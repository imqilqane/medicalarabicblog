from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from  django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100 ,verbose_name='العنوان')
    image = models.ImageField (default='' , upload_to='post_pics' ,verbose_name='الصورة')
    content = models.TextField(default='' ,verbose_name='المحتوى')
    post_date = models.DateTimeField(default = timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User , default='imqi', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detiels' , args=[self.pk])

    class Meta:
        ordering = ('-post_date',)

class Comment(models.Model):
    name = models.CharField(max_length=50 , verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الاكتروني')
    body = models.TextField(default=None , verbose_name='نص التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE ,default=None, related_name='comments') #had ta3li9 dyal axmn post

    def __str__(self):
        return  ' علق {} على {} '.format(self.name ,self.post)

    class Meta:
        ordering = ('-comment_date',)



# daba ghadi nst3mlo
#python manage.py makemigrations
#python manage.py migrate
