from django.db import models

# Create your models here.
class Product(models.Model):
    """ adding multiple images """
    title = models.CharField(max_length=250, default='')
    image_01 = models.ImageField(upload_to='images', blank=True)
    image_02 = models.ImageField(upload_to='images', blank=True, null=True)
    image_03 = models.ImageField(upload_to='images', blank=True, null=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    size = models.CharField(max_length=100, default='')
    colour = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    flex = models.CharField(max_length=100, default='')
    shape = models.CharField(max_length=100, default='')
    rider_prodile = models.CharField(max_length=100, default='')
    board_proflie = models.CharField(max_length=100, default='')
    condition = models.CharField(max_length=100, default='')
   
    def __str__(self):
        return self.name