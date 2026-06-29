from django.contrib import admin

from .models import Category, OperationType, Record, Status, Subcategory

admin.site.register(Status)
admin.site.register(OperationType)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Record)

admin.site.site_header = "Администрирование ДДС"
admin.site.site_title = "ДДС"
admin.site.index_title = "Панель управления"
