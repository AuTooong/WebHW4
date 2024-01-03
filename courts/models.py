from django.db import models

# Create your models here.
class Court(models.Model):
    COURT_TYPE = [
        ("G", "草地"),
        ("H", "硬地"),
        ("N", "泥地"),
        ("D", "地毯"),
    ]
    courtname = models.CharField(null=True,max_length=100)
    courttype = models.CharField(null=True,max_length=1, 
                                 choices=COURT_TYPE)
    city = models.CharField(null=True,max_length=100)

