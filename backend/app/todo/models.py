from django.db import models

# Create your models here.

class Todo(models.Model):
      title = models.CharField(max_length=256)
      description = models.TextField()
      completed = models.BooleanField(default=False)

      def _str_(self):
        return self.title

class Branch(models.Model):
    class Meta:
        verbose_name_plural = 'branches'
    bank_name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    def __str__(self):
        return(f"{self.bank_name}")


class Customer(models.Model):
    customer_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    def __str__(self):
        return(f"{self.customer_name}")