from django.db import models

# Create your models here.

class TestModel(models.Model):
    test_name = models.CharField( max_length = 300 )
    test_description = models.TextField( max_length = 2000 )

