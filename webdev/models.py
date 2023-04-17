from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    publisher_name = models.CharField(max_length=200)
    publisher_age = models.IntegerField()
    page_number = models.IntegerField()
    publish_date = models.DateField()
    book_type = models.BooleanField(default=True)