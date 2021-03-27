from django.contrib import admin
from .models import Law, DailyId

# Register your models here.
admin.site.register(Law)


class DailyIdAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        base_add_permission = super(DailyIdAdmin, self).has_add_permission(request)
        if base_add_permission:
            count = DailyId.objects.all().count()
            if count == 0:
                return True
            return False


admin.site.register(DailyId, DailyIdAdmin)
