from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add 'form-control' class to all form fields
        for field in self.fields.values():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control contact-input' 
        

    class Meta:
        model = Order
        exclude = ('paid',)