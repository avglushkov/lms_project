from django.contrib import admin
from users.models import User, Payment
# Register your models here.


#
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'payment_date')