from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),

    path('company/id/<int:company_id>/', views.CompanyDetailView.as_view(), name='company_details'),
        
    path('device/id/<int:device_id>/', views.DeviceDetailView.as_view(), name='device_details'),   
    path('device/create/', views.DeviceCreateView.as_view(), name='device_create'),
    path('company/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('add-employee/', views.EmployeeCreateView.as_view(), name='employee_create'),



    path('device/<int:pk>/update/', views.DeviceUpdateView.as_view(), name='device_update'),
   
    path('checkout', views.CheckoutView.as_view(), name='checkout_device'),    
    path('return/<int:checkout_log_id>/', views.ReturnView.as_view(), name='return_device'),
    
    path('login/', views.LoginPage.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
