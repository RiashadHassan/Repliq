from django.contrib import admin
from .models import Company, Employee, Device, CheckoutLog, Staff

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(CheckoutLog)
admin.site.register(Staff)
