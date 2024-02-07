from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Company, Employee, Device, CheckoutLog
from .forms import DeviceForm, CheckoutForm

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
       
