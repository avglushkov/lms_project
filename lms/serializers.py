from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from lms.models import Course, Lesson, Subscription
from lms.validators import validators_video_link





class LessonSerializer(serializers.ModelSerializer):

    video_link = serializers.CharField(validators=[validators_video_link], read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()
    subscription = SerializerMethodField(read_only=True)

    def get_lessons_count(self, instance):
        return instance.lesson_set.all().count()

    def get_lessons(self,course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_subscription(self, instance):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user, course=instance).exists()


    class Meta:
        model = Course
        fields = ('id', 'name', 'preview', 'description','lessons_count','lessons','owner', 'subscription')

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('__all__')