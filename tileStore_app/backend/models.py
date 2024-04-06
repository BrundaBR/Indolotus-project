from django.db import models

# Create your models here.
class Tileproducts(models.Model):
    id=models.AutoField(primary_key=True)
    tileName=models.CharField(max_length=255)
    description=models.CharField(max_length=955)
    cost=models.FloatField()
    typeoftile=models.CharField(max_length=255)
    lenghtoftile=models.CharField(max_length=20)
    image=models.ImageField(upload_to='tile_products/Images',default="")

class Projects(models.Model):
    id=models.AutoField(primary_key=True)
    projectName=models.CharField(max_length=255)
    description=models.CharField(max_length=955)
    image=models.ImageField(blank=True,upload_to='projects/Images',default="")
