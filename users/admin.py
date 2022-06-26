from django.contrib import admin
from .models import Domain, Profile


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    pass
