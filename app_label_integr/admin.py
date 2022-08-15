from django.contrib import admin
from .models import BufferFood, СompoundSettings

class IntegrAdmin(admin.ModelAdmin):
    pass


admin.site.register(BufferFood, IntegrAdmin)
admin.site.register(СompoundSettings, IntegrAdmin)

