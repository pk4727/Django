from django.db import models

# Create your models here.
class service_custom(models.Model):
    service_1 = models.CharField(max_length=50)
    service_2 = models.CharField(max_length=50)
    service_des = models.TextField()