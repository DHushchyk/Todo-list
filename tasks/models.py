from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

