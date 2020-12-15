from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"


class Journal(models.Model):
    title = models.CharField(max_length=120,)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    categories = models.ManyToManyField(Category,)
    publish_date = models.DateField(auto_now_add=False,)
    views = models.IntegerField(default=0,)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"
