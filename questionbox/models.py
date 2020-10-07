from django.db import models
from users.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    # 
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Answer(models.Model):
    body = models.TextField(null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.body}"
