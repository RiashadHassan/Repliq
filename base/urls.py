from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='device_list'),
    path('device/id/<int:device_id>/', views.DeviceDetailView.as_view(), name='device_detail'),
    
    path('device/create/', views.DeviceCreateView.as_view(), name='device_create'),
    path('device/<int:pk>/update/', views.DeviceUpdateView.as_view(), name='device_update'),
    
    # path('device/<int:device_id>/checkout/', views.CheckoutDeviceView.as_view(), name='checkout_device'),
    # path('device/<int:device_id>/return/', views.ReturnDeviceView.as_view(), name='return_device'),
    
    path('login/', views.LoginPage.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
