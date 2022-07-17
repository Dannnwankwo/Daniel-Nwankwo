from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max-length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
    

