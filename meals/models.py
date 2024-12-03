from django.db import models


class Meal(models.Model):
    MEAL_CHOICES = [
        ('Select Type','Select Type'),
        ('Appetizer','Appetizer'),
        ('Main Course','Main Course'),
        ('Dessert','Dessert')
    ]

    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=15, choices=MEAL_CHOICES)
    cuisine = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}: {self.price}"