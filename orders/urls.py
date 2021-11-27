from django.urls import path
from orders.views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView, OrderReadView
from orders.views import order_forming_complete, get_product_price

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('forming/complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('read/<int:pk>/', OrderReadView.as_view(), name='order_read'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('product/<int:pk>/price/', get_product_price)
]
