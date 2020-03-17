from django.db import models

# Create your models here.
class Product(models.Model):
    """ adding multiple images """
    name = models.CharField(max_length=250, default='')
    product_image_01 = models.ImageField(upload_to='images', blank=True)
    product_image_02 = models.ImageField(upload_to='images', blank=True, null=True)
    product_image_03 = models.ImageField(upload_to='images', blank=True, null=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
   
    def __str__(self):
        return self.name