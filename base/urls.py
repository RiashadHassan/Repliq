from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='device_list'),
    path('device/<int:device_id>/', views.DeviceDetailView.as_view(), name='device_detail'),
    path('device/create/', views.DeviceCreateView.as_view(), name='device_create'),
    path('device/<int:pk>/update/', views.DeviceUpdateView.as_view(), name='device_update'),
    # path('device/<int:pk>/delete/', views.DeviceDeleteView.as_view(), name='device_delete'),
    # path('device/<int:device_id>/checkout/', views.CheckoutDeviceView.as_view(), name='checkout_device'),
    # path('device/<int:device_id>/return/', views.ReturnDeviceView.as_view(), name='return_device'),
]
