from django.db import models

# Create your models here.
class Emp(models.Model):
    emp_name = models.TextField()
    emp_email = models.EmailField()
    emp_mobile = models.TextField()
