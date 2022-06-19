from django.contrib import admin

# Register your models here.
from .models import  Description, Title

admin.site.register(Title)
admin.site.register(Description)