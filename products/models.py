from django.db import models

# Create your models here.
class Category(models.Model):
    snowboard_category = models.CharField(max_length=250, unique=True)
    category_description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to='category', blank=True)
    category_slug = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.snowboard_category

class Product(models.Model):
    """ adding multiple images """
    title = models.CharField(max_length=250, default='')
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    image_01 = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=100, default='')
    colour = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    flex = models.CharField(max_length=100, default='')
    shape = models.CharField(max_length=100, default='')
    rider_profile = models.CharField(max_length=100, default='')
    board_profile = models.CharField(max_length=100, default='')
    condition = models.CharField(max_length=100, default='')
    stock = models.IntegerField(blank=True)
    available = models.BooleanField(default=True)
   
    def __str__(self):
        return self.title

