from django.contrib import admin
from .models import SecurityProfile


@admin.register(SecurityProfile)
class SecurityProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "question",
    )
