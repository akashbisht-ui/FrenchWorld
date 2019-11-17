from django.db import models

# Create your models here.
class French(models.Model):
    name= models.TextField(max_length=100)
    engname= models.TextField(max_length=100)