from django.contrib import admin

from blogs import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
