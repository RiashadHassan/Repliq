from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

from .models import Company, Employee, Device, CheckoutLog, Staff
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


class Home(View):
    template_name='home.html'
    
    def get(self, request):
        devices = Device.objects.all()
        companies = Company.objects.all()
        checked_out_devices = CheckoutLog.objects.all()
        context = {'devices': devices, 'companies': companies, 'checked_out_devices':checked_out_devices}
        return render(request, self.template_name, context)
class DeviceDetailView(View):
    template_name='device_details.html'
    page = 'device_details'

    
    def get(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        context= {'device': device, 'page': self.page}
        return render(request, self.template_name, context)
    
    def post(self, request, device_id):
        device = get_object_or_404(Device, pk=device_id)
        device.delete()
        return redirect('home')

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
            return redirect('home')
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
    

class CompanyDetailView(View):
    template_name = 'device_details.html'
    page = 'company_details'
    
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        employees=Employee.objects.filter(company=company)
        context={'company': company, 'employees': employees, 'page': self.page}
        return render(request, self.template_name,context)

class DeviceCheckoutView(View):
    template_name = 'checkout_device.html'

    def get(self, request):
        form = CheckoutForm()
        context= {'form': form}
        return render(request, self.template_name,context)

    def post(self, request):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                staff_member = Staff.objects.get(user=request.user)
                
            except ObjectDoesNotExist:
                return HttpResponse("You don't have permission to perform this action.")
            
            checkout_instance = form.save(commit=False)
            checkout_instance.assigned_by = staff_member
            
            device_id= form.cleaned_data['device']
            device = Device.objects.get(id=device_id.id)
            device.checked_out=True
            device.save()
            
            checkout_instance.device= device
            checkout_instance.employee= form.cleaned_data['employee']
             
            checkout_instance.save()
            
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)
    