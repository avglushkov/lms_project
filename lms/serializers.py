from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from lms.models import Course, Lesson





class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lessons_count(self, instance):
        return instance.lesson_set.all().count()

    def get_lessons(self,course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]


    class Meta:
        model = Course
        fields = ('id', 'name', 'preview', 'description','lessons_count','lessons','owner')