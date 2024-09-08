import datetime
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta, datetime


from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from lms.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from lms.models import Course, Lesson, Subscription
from lms.paginators import LmsPaginator
from users.permissions import IsModerator, IsOwner
from lms.tasks import change_course_sendmail



class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LmsPaginator

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [~IsModerator]
        elif self.action == 'update':
            self.permission_classes = [IsModerator | IsOwner]
        elif self.action == 'retrive':
            self.permission_classes = [IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [~IsModerator | IsOwner]

        return super().get_permissions()

    def perform_update(self, serializer):
        """проверка наличия изменений"""

        course = serializer.save()
        if course.last_change:
            if timezone.now() - course.last_change > timedelta(hours=4):
                change_course_sendmail.delay(course)
        else:
            change_course_sendmail.delay(course)
        course.last_change = timezone.now()
        course.save()



class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LmsPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


# class SubscriptionViewSet(viewsets.ModelViewSet):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request, *args, **kwargs):
#         user = self.request.user
#         course_id = self.request.data.get("course")
#         course_item = get_object_or_404(Course, pk=course_id)
#
#         subscription, created = Subscription.objects.get_or_create(user=user, course=course_item)
#         if not created:
#             subscription.delete()
#             message = 'Subscription removed'
#         else:
#             message = 'Subscription added'
#
#         return Response({"message": message})
class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)
    # queryset = Subscription.objects.all()
    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course = get_object_or_404(Course, pk=course_id)
        sub_item = Subscription.objects.filter(user=user, course=course)

        if sub_item.exists():
            sub_item.delete()
            message = 'Подписка отключена'

        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка включена'

        return Response({'message': message})
