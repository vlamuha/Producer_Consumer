from datetime import datetime

import telebot
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from producer_consumer.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(employee=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = self.get_queryset()
        return context


@login_required
def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()

    message = f"Задача No{pk}-{task_id} під назвою {name} була опрацьована {employee} у {datetime} ".format(
        pk=order.pk,
        task_id=order.task_id,
        name=order.name,
        employee=f"{order.employee.first_name} {order.employee.position}",
        datetime=datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
    )

    bot = telebot.TeleBot(token="BOT_API_KEY")

    bot.send_message(chat_id=order.employee.username, text=message)

    return redirect("orders")
