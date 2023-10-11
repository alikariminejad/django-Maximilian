from django.contrib import admin
from .models import Post, Tag, Author

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
