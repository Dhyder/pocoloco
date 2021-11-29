from django.contrib import admin

# Register your models here.
from .models import Editor,Category,Location,Image

admin.site.register(Editor)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)
