from django.db import models


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


class JournalManager(models.Manager):
    def smaller_than(self, count):
        return self.filter(views__lte   =count)

    def author(self, name):
        return self.filter(author__name__icontains=name)


class Journal(models.Model):
    title = models.CharField(max_length=120,)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    categories = models.ManyToManyField(Category,)
    publish_date = models.DateField(auto_now_add=False,)
    views = models.IntegerField(default=0,)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"

    objects = JournalManager()
