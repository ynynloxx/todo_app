from django.contrib import admin

from .models import Category, ToDo, Appointment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('todo', 'appointment',)
    list_filter = ('category',)


admin.site.register(Category)
admin.site.register(ToDo)
admin.site.register(Appointment)
