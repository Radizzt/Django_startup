#IMPORTANT. Lesson on chapter 02_05 is done in here as well
from django.contrib import admin
#import models module in the inventory app
from .models import Item

#ModelAdmin lets you customize the admin GUI
class ItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'amount']#display certain attribute as the title


#Register the model with the custom list display class
admin.site.register(Item, ItemAdmin);
