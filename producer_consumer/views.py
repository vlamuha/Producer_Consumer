from datetime import datetime

import telebot
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView

from producer_consumer.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "producer_consumer/order_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(employee=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders_list = Order.objects.filter(employee=self.request.user)
        context["orders_list"] = orders_list
        return context


@login_required
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('producer_consumer:order_list')


def send_message(request, pk):
    order = Order.objects.get(pk=pk)
    employee = order.employee
    message = f"Задача No{pk}-{order.task_id} під назвою {order.name} була опрацьована {employee.first_name}" \
              f" {employee.position} у {datetime.datetime.now()}"

    return HttpResponse(message)
