from celery import shared_task
from random import choice
from .models import Order, Employee


@shared_task
def create_order(task_id, name, description):
    employees = Employee.objects.all()
    selected_employee = choice(employees)
    Order.objects.create(
        task_id=task_id, name=name, description=description, employee=selected_employee
    )
