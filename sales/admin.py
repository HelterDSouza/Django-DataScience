from django.contrib import admin

from .models import CSV, Position, Sale

# Register your models here.


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Sale)
class SalesAdmin(admin.ModelAdmin):
    pass


@admin.register(CSV)
class CSVAdmin(admin.ModelAdmin):
    pass
