from django.contrib import admin
from .models import Supplier, Range, Roll, Cut

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Range)
admin.site.register(Cut)
admin.site.register(Roll)
