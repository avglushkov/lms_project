from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonDestroyAPIView, \
    LessonRetriveAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/<int:pk>/', LessonRetriveAPIView.as_view(), name='lesson-get'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

              ] + router.urls
