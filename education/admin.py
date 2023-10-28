from django.contrib import admin

from education.models import Lesson, Payment, Subscription, Course

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Payment)
admin.site.register(Subscription)
admin.site.register(Course)