from django.contrib import admin

from .models import Category, OperationType, Record, Status, Subcategory


admin.site.register(Status)
admin.site.register(OperationType)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Record)
