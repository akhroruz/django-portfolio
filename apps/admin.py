from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import User, Project, ImageList, Category, Skill


@admin.register(User)
class UserAdmin(ModelAdmin):
    exclude = (
        'groups', 'user_permissions', 'active', 'last_login', 'is_active', 'is_staff', 'is_superuser',
        'date_joined',
        'password', 'username')


class ImageAdmin(StackedInline):
    model = ImageList


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    inlines = [ImageAdmin]
    exclude = ('slug', 'image')


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = ('slug',)


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    pass
