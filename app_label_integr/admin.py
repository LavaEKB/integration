from django.contrib import admin
from .models import BufferFood, ConnectSettings

class IntegrAdmin(admin.ModelAdmin):
    pass


admin.site.register(BufferFood, IntegrAdmin)
admin.site.register(ConnectSettings, IntegrAdmin)


