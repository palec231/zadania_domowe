from django.db import models

# Zadanie 1
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

# Zadanie 8
class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(       # Zadanie 1
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(Tag, related_name='posts',blank=True)  # Zadanie 8
    def __str__(self):
        return self.title