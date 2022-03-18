import uuid

from django.db import models


# Create your models here.
class User_Face(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=3, default='A')
    age = models.CharField(max_length=60, default='10')
    password = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=15, default='000000')

    def __str__(self):
        return self.name
