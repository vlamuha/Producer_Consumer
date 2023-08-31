from django.contrib import admin
from .models import Order, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "position")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("task_id", "name", "employee")
    search_fields = ("task_id", "name", "employee__first_name", "employee__last_name")
