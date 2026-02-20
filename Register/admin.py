from django.contrib import admin

# Register your models here.
from . models import Register_Master
admin.site.register(Register_Master)

# python manage.py makemigrations
#  python manage.py migrate  