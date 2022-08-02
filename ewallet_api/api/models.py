from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

class History(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
