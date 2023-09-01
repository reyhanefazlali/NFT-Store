from django.contrib import admin
from web.models import Create, Category, Collection


class CreateAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'Active']
    search_fields = ['title', 'price']
    list_filter = ['Active', 'email']


admin.site.register(Create, CreateAdmin)
admin.site.register(Category)
admin.site.register(Collection)
