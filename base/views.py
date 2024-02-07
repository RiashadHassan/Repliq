from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import Company, Employee, Device, CheckoutLog
from .forms import DeviceForm, CheckoutForm

class RegisterPage(View):
    template_name= 'login_register.html'
    page='register'
    
    def get(self,request):
        form = UserCreationForm()
        context={'page':self.page, 'form': form}
        return render(request, self.template_name, context)
    
    def post(self,request):  
        form=UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
        context={'page':self.page, 'form': form}
        return render(request, self.template_name, context)

class LoginPage(View):
    template_name='login_register.html'
    page='login'
    
    def get(self,request):
        context= {'page':self.page}
        return render(request, self.template_name, context)
                
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('NO')
    

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('home')


class DeviceListView(View):
    template_name='device_list.html'
    
    def get(self, request):
        devices = Device.objects.all()
        context = {'devices': devices}
        return render(request, self.template_name, context)

class DeviceDetailView(View):
    template_name='device_details.html'
    
    def get(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        context= {'device': device}
        return render(request, self.template_name, context)
    
    def post(self, request, device_id):
        device = get_object_or_404(Device, pk=device_id)
        device.delete()
        return redirect('device_list')

class DeviceCreateView(View):
    template_name='device_form.html'
    def get(self, request):
        form = DeviceForm()
        context ={'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
        context={'form': form}
        return render(request, self.template_name, context)

class DeviceUpdateView(View):
    template_name='device_form.html'
    def get(self, request, device_id):
        device = get_object_or_404(Device, pk=device_id)
        form = DeviceForm(instance=device)
        context={'form': form}
        return render(request, self.template_name, context)

    def post(self, request, device_id):
        device = get_object_or_404(Device, pk=device_id)
        form = DeviceForm(request.POST, instance=device)
    
class CompanyListView(View):
    template_name = 'device_list.html'
    
    def get(self, request):
        companies = Company.objects.all()
        return render(request, self.template_name, {'companies': companies})

class CompanyDetailView(View):
    template_name = 'company_detail.html'
    
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        devices = company.devices.all()
        return render(request, self.template_name, {'company': company, 'devices': devices})
