from django.contrib import admin
from .models import BufferFood, СompoundSettings

class IntegrAdmin(admin.ModelAdmin):

    change_list_template = 'admin/app_label_integr/change_list.html'

    def changelist_view(self, request, extra_context=None):
        
        return super(IntegrAdmin, self).changelist_view(request)

admin.site.register(BufferFood, IntegrAdmin)
admin.site.register(СompoundSettings, IntegrAdmin)

