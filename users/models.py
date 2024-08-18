from django.db import models
from django.contrib.auth.models import AbstractUser
from lms.models import Course, Lesson

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='телефон')
    town = models.CharField(max_length=50, blank=True, null=True, verbose_name='город')
    avatar = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='аватар')
    code = models.CharField(max_length=100, blank=True, null=True, verbose_name='токен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        # permissions = [("can_deactivate_user", "Can deactivate user",)]

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True, verbose_name='Дата платежа')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Оплаченный курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Оплаченный урок')
    summ = models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма')
    payment_type = models.CharField(max_length=20, choices=[('cash', 'Наличные'), ('transaction', 'Перевод на счет')],
                                    blank=True, null=True, verbose_name='Способ платежа')

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f'{self.user} - {self.payment_date}'