from django.forms import ModelForm
from .models import Device, CheckoutLog, Company, Employee

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude= ['checked_out']
        
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields= '__all__'
        
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields= '__all__'
        
class CheckoutForm(ModelForm):
    class Meta:
        model = CheckoutLog
        fields = ['device', 'employee']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)      
        
        self.fields['device'].queryset = Device.objects.filter(checked_out=False)