from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Product(models.Model):
    CHOICE = (
        ('all_mountain', 'All Mountain'),
        ('big_mountain', 'Big Mountain'),
        ('freestyle', 'Freestyle'),
        ('pipe_park', 'Pipe/Park'),
        ('jib_street', 'Jib/Street'),
        ('boardercross', 'Boardercross')
    )
        
    name = models.CharField(max_length=250, default='')
    slug = models.SlugField(max_length=200, unique=True)
    image_01 = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=100, default='')
    colour = models.CharField(max_length=100, default='')
    flex = models.CharField(max_length=100, default='')
    shape = models.CharField(max_length=100, default='')
    board_profile = models.CharField(max_length=100, default='')
    stock = models.IntegerField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Product, self).save(*args, **kwargs)

