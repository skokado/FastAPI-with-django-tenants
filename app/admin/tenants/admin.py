from django.contrib import admin
from django.core.management import call_command
from django_tenants.admin import TenantAdminMixin

from tenants import models

# Register your models here.

@admin.register(models.Company)
class CompanyAdmin(TenantAdminMixin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # テナントの手動追加時にスキーママイグレーション(テーブルを作成)する
        super().save_model(request, obj, form, change)
        call_command('migrate_schemas')


@admin.register(models.Domain)
class DomainAdmin(admin.ModelAdmin):
    pass
