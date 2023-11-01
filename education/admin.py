from django.contrib import admin

from education.models import Lesson, Subscription, Course

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Subscription)
admin.site.register(Course)