from rest_framework import serializers

from education.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.paid_course:
            course_data = CourseSerializer(instance.paid_course).data
            data['course'] = course_data
        elif instance.paid_lesson:
            lesson_data = LessonSerializer(instance.paid_lesson).data
            data['lesson'] = lesson_data

        return data