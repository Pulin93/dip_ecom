from django.db import models

# Create your models here.
class FeedbackData(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    feedback = models.CharField(max_length=264)
