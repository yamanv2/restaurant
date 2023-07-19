from django.db import models

# Create your models here.


class Ingredient(models.Model):

    UNIT_CHOICE = (
        ('tbsp', 'tbsp'),
        ('gram', 'Gram'),
        ('kg', 'KiloGram'),
        ('mg', 'MiliGram'),
        ('unit', 'Unit'),
    )

    ingredient_name = models.CharField(max_length=200, null=True)
    available_quantity = models.FloatField(null=True)
    unit = models.CharField(max_length=5, null=True, choices=UNIT_CHOICE)
    unit_price = models.FloatField(null=True)

    def __str__(self):
        return self.ingredient_name



class MenuItem(models.Model):
    item_name = models.CharField(max_length=200, null=True)
    set_price = models.FloatField(null=True)

    def __str__(self):
        return self.item_name



class RecipeRequirement(models.Model):

    UNIT_CHOICE = (
        ('tbsp', 'tbsp'),
        ('gram', 'Gram'),
        ('kg', 'KiloGram'),
        ('mg', 'MiliGram'),
        ('unit', 'Unit'),
    )
    
    menu_item = models.ForeignKey(MenuItem, null=True, on_delete=models.SET_NULL)
    ingredient = models.ForeignKey(Ingredient, null=True, on_delete=models.SET_NULL)
    quantity = models.FloatField(null=True)
    unit = models.CharField(max_length=5, null=True, choices=UNIT_CHOICE)

    def __str__(self):
        return self.ingredient.ingredient_name



class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.menu_item.item_name