from django.contrib import admin

from .models import SupervisorMenuItem, SupervisorSubMenuItem


@admin.register(SupervisorMenuItem)
class SupervisorMenuItemAdmin(admin.ModelAdmin):
    pass


@admin.register(SupervisorSubMenuItem)
class SupervisorSubMenuItemAdmin(admin.ModelAdmin):
    pass
