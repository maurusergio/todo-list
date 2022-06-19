from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('deadline')
    
    def __str__(self):
        return self.title_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Description(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=500)
   

    def __str__(self):
        return self.description_text