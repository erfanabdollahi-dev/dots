from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# Register your models here.
class UserAdminConfig(UserAdmin):
    model = User
    # فقط فیلدهایی که در مدل خودت داری
    list_display = ('username', 'email', 'phone', 'is_active', 'is_staff')


    # فیلدهای فرم ادمین برای ویرایش کاربر
    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone', 'password', 'birthDate', 'image', 'is_active', 'is_staff')}),
    )


admin.site.register(User, UserAdminConfig)
admin.site.unregister(Group)