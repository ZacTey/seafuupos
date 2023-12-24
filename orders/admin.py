from django.contrib import admin
from .models import Category, Fish, UserOrder, SavedCarts, Table
from tinymce.widgets import TinyMCE
from django.db import models

class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class RegularPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

admin.site.register(Category,CategoryAdmin)
admin.site.register(Fish)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
admin.site.register(Table)