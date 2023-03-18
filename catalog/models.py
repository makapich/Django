from django.db import models


class City(models.Model):
    city = models.CharField('City', max_length=150)


class Product(models.Model):
    product = models.CharField('Product', max_length=150)
    price = models.FloatField('Price', max_length=150)


class Person(models.Model):
    name = models.CharField('Name', max_length=150)
    email = models.CharField('Email', max_length=150)
    suppliers = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Provider(models.Model):
    provider = models.CharField(max_length=50)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        primary_key=True
    )

