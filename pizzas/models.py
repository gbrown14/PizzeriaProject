from django.db import models


# Create your models here.

#pizza
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.pizza_name


#toppings
class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=50)

    def __str__(self):
        return self.topping_name


#comments
class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text