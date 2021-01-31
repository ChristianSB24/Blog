from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Post, CustomUser

@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
	pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	fields = (
		"author", "title", "entry", "created_at", "updated_at",
	)
	list_display = (
		"author", "title", "Entry", "created_at", "updated_at",
	)
	readonly_fields = (
		"created_at", "updated_at",
	)

# Register your models here.
