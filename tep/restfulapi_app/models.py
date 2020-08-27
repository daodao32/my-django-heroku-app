from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
