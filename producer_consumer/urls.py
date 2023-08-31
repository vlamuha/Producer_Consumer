from django.urls import path
from . import views
from .views import OrderListView

urlpatterns = [
    path("orders/", OrderListView.as_view(), name="order_list"),
    path("orders/delete/<int:order_id>/", views.delete_order, name="delete_order"),
]
