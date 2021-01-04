from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Products(models.Model):
    title=models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    image=models.ImageField(upload_to='templates/images')
    price=models.IntegerField()
    created_At = models.DateField(auto_now_add=True)
    updated_At = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

class Orders(models.Model):
    PAYMENT_CHOICES = (
        ("cash", "cash"),
        ("paytm", "paytm"),
        ("card", "mastercard"),
        ("phonepay", "phonepay"),

    )
    STATUS_CHOICES=(
        ('new','new'),
        ('paid','paid')
    )

    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    total =models.IntegerField()
    products = models.ManyToManyField(Products)
    created_At = models.DateField(auto_now_add=True)
    updated_At = models.DateField(auto_now=True)
    status= models.CharField(max_length=20,choices=STATUS_CHOICES)
    mode_of_payment=models.CharField(max_length=20,choices=PAYMENT_CHOICES)
    def __str__(self):
        return f"{self.user_id}-{User.username}"

class Orders_items(models.Model):
    order_id=models.ForeignKey(Orders,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return f"{self.product_id}"
    # def total(self):
    #     total=self.Quantity * self.price