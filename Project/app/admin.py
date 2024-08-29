from django.contrib import admin
from .models import Course, Lecture


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'count')
    search_fields = ('title',)



class LectureAdmin(admin.ModelAdmin):
    list_display = ('user', 'age')
    search_fields = ('user__username',)
admin.site.register(Course)
admin.site.register(Lecture)