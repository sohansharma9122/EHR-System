from django.contrib import admin
from .models import Laboratory_test
# Register your models here.
class changetest(admin.ModelAdmin):
    fields=['test_Price','test_name']
    search_fields=['test_name']
    list_filter=['test_Price',"test_name"]
    list_display=['test_Price',"test_name"]
    list_editable=['test_name']
    
admin.site.register(Laboratory_test,changetest)

