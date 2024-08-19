from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='owner_category')
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("shop:category_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True, editable=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products_category')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='owner_product')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_comment')
    text = models.TextField()
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.created_at}"