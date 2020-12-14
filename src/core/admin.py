from django.contrib import admin
from core.models import Category, Author, Journal

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Journal)
