from django.conf import settings
from django.db import models
import uuid
class Video(models.Model):

    Videofile = models.ImageField(upload_to=str(uuid.uuid4()), default=None, blank=True, null=True)

    class Category(models.TextChoices):
        Music = 'music'
        Movie = 'movie'
        Drama = 'drama'
       
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    video_key = models.CharField(max_length=12, null=True, blank=True)
    likes_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='likes_user')
    upload_date = models.DateTimeField(auto_now_add=True, null=True, blank=True) # first created date
    category = models.TextField(choices=Category.choices, blank=True, null= True)

    class Meta:
        ordering = ['-upload_date']

    def count_likes_user(self):
        return self.likes_user.count()

    def __str__(self):
        return self.title
    