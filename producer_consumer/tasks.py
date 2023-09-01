from celery import Celery
from django.core.management.base import BaseCommand
from django.conf import settings

from producer_consumer.models import Order, Employee


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        celery_app = Celery(
            app_name=settings.CELERY_APP_NAME,
            broker=settings.CELERY_BROKER_URL,
            backend=settings.CELERY_RESULT_BACKEND,
        )

        @celery_app.task(name='add_order')
        def add_order():
            employee = Employee.objects.filter(probation=False).order_by('?').first()

            order = Order(
                task_id=1,
                name='Задача No1',
                description='Це перша задача',
                employee=employee,
            )
            order.save()

        celery_app.send_task('add_order')
