
from django.contrib import admin

from .models import Award
# Register your models here.

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    pass