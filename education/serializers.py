from rest_framework import serializers
from education.models import Course, Lesson, Subscription
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(source='is_subscribed', read_only=True, many=True)
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    number_of_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_number_of_lessons(self, instance):
        return instance.lesson_set.count()
