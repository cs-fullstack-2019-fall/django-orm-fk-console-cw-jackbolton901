
from django.db import models


class Author(models.Model):
    lastName = models.CharField
    firstName = models.CharField

    def __str__(self):
        return self.lastName


class Post(models.Model):
    title = models.CharField
    content = models.CharField
    date_posted = models.DateTimeField
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title