from django.forms import ModelForm
from .models import Device, CheckoutLog

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields= '__all__'
        
        
class CheckoutForm(ModelForm):
    class Meta:
        model = CheckoutLog
        fields = ['device', 'employee']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)      
        
        self.fields['device'].queryset = Device.objects.filter(checked_out=False)