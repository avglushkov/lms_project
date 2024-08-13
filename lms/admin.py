from django.contrib import admin
from lms.models import Course, Lesson

# Register your models here.
@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk','name')

@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk','name')