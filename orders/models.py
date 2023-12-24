from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    category_title = models.CharField(max_length=200)
    category_gif = models.ImageField(upload_to="media")
    category_description = models.TextField() #make this the wysiwyg text field
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"{self.category_title}"

    def has_add_permission(self):
        return False



class Fish(models.Model):
    dish_name = models.CharField(max_length=200)
    fried_price = models.DecimalField(max_digits=6, decimal_places=2)
    steam_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "List of Fish"
        verbose_name_plural = "List of Fish"

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Fish : {self.dish_name}"

class UserOrder(models.Model):
    username = models.CharField(max_length=200) #who placed the order
    order = models.TextField() #this will be a string representation of the cart from localStorage
    table = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2) #how much was the order
    time_of_order  = models.DateTimeField(default=datetime.now, blank=True)
    delivered = models.BooleanField()

    class Meta:
        verbose_name = "User Order List"
        verbose_name_plural = "User Order List"

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Order placed by  : {self.username} on {self.time_of_order.date()} at {self.time_of_order.time().strftime('%H:%M:%S')}"

class SavedCarts(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    cart = models.TextField() #this will be a string representation of the cart from localStorage

    class Meta:
        verbose_name = "Saved Users Cart"
        verbose_name_plural = "Saved Users Cart"

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Saved cart for {self.username}"

class Table(models.Model):
    table_no = models.IntegerField(primary_key=True) #this will be a int representation of the cart from localStorage
    table_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Table No"
        verbose_name_plural = "Table No"


    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Table number for {self.table_no}"