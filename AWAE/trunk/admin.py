from django.contrib import admin
# Register your models here.
from ordered_model.admin import OrderedModelAdmin
from .models import Trunk, EyeKey
# Register your models here.

class EyeKeyAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links', 'label', 'trunk', 'row', 'col', 'col_size')


admin.site.register(Trunk)
admin.site.register(EyeKey, EyeKeyAdmin)
