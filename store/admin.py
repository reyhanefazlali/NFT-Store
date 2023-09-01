from django.contrib import admin
from store.models import Post, Author, BidDetail

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'Active']
    search_fields = ['title', 'content']
    list_filter = ['Artist', 'Active']


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(BidDetail)
