from django.db import models

# Create your models here.
class Author(models.Model):
    id=models.IntegerField(primary_key=True)
    author_name=models.CharField(max_length=255)
    author_dis=models.TextField()

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=255)
    book_dis=models.CharField(max_length=255)
    author_id=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')