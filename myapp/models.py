from django.db import models
from tinymce_4.fields import TinyMCEModelField

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='Products/',blank=True,null=True)
    content = TinyMCEModelField(blank=True,null=True)


class Contact(models.Model):
    bu_type = (
        ('Distributor','Distributor'),
        ('Wholesaler','Wholesaler'),
        ('Private label','Private label'),
        ('Other','Other')
    )

    business_type = models.CharField(max_length=255,choices=bu_type)
    business_name = models.CharField(max_length=255,choices=bu_type)
    established_year = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

