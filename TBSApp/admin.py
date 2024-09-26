from django.contrib import admin
from .models import UserRegister,Routes,payment,Booking
# Register your models here.

admin.site.register(UserRegister)
admin.site.register(Routes)
admin.site.register(payment)
admin.site.register(Booking)