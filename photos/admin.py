from django.contrib import admin
from .models import Location,Category,Gallery


# Register your models here.
admin.site.register(Gallery)
admin.site.register(Location)
admin.site.register(Category)
