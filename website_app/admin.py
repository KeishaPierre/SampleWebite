from django.contrib import admin
from website_app.models import Products, User, Category

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Products)


