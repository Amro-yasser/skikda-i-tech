from django.contrib import admin
from .models import Post,Author,Category,Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)