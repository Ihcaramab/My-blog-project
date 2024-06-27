from django.db import models
from account.models import User
from django.utils.translation import gettext_lazy as _ #It is used for translation
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    ) 
    #It's not going to be added automatically. You'll be the one to add the date you want.

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs) #It adds the slug for us automatically

    def __str__(self):
        return f"category for {self.name}"

class Product(models.Model):
    category = models.ForeignKey(
        "products.Category", 
        verbose_name=("Product Categories"), 
        on_delete=models.CASCADE, null=True, blank=True
    ) 
    #Whenever a product is deleted, it is also going to be deleted in the category or whenever a category is deleted, it is also going to be deleted in the product.
    user = models.ForeignKey(User, verbose_name=_("User"), null=True, on_delete=models.SET_NULL) 
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True) #8000/blog/detail/my-shoe
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="media", null=True, blank=True)

