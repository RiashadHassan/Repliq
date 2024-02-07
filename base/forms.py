from django.forms import ModelForm
from .models import Device, CheckoutLog

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields= '__all__'
        
        
class CheckoutForm(ModelForm):
    class Meta:
        model = CheckoutLog
        fields= '__all__'