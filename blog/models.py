from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.FileField(upload_to='static/img', blank=True)
    created_at = models.DateTimeField()

    def __str__(slef):
        return slef.title