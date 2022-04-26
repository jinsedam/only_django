from django.contrib import admin
from . import models


@admin.register(models.InterestingClubList)
class InterestingClubListAdmin(admin.ModelAdmin):
    pass

@admin.register(models.InterestingPostList)
class InterestingPostListAdmin(admin.ModelAdmin):
    pass