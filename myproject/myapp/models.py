from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Поле для зображення

    def __str__(self):
        return self.title