from django.db import models

# Create your models here.
class contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    contact = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email

