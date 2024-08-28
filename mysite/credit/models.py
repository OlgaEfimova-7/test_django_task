from django.db import models

# Create your models here.

class Contract(models.Model):
    created = models.DateTimeField(auto_now_add=True)

class CreditRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

class Producer(models.Model):
    created = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    credit_request = models.ForeignKey(CreditRequest, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

