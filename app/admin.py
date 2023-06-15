from django.contrib import admin
from .models import *


# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'active')


admin.site.register(Pizza, PizzaAdmin)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Ingredient, IngredientAdmin)
