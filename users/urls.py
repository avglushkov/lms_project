from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListAPIView, PaymentCreateAPIView, PaymentDestroyAPIView, \
    PaymentUpdateAPIView, PaymentRetriveAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [

                  path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
                  path('payment/<int:pk>/', PaymentRetriveAPIView.as_view(), name='payment-get'),
                  path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
                  path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment-delete'),

              ] + router.urls
