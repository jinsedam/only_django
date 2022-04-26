from django.contrib import admin
from . import models


@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
