from django.contrib import admin
from .models import Supplier, Range, Cut

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Range)
admin.site.register(Cut)
