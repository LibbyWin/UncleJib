from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content
