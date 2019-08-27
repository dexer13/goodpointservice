from django.forms import *

from stores.models import Store, Sale


class StoreForm(ModelForm):
    class Meta:
        model=Store
        fields='__all__'

    nombre=CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    correo=EmailField(required=True, widget=EmailInput(attrs={'class': 'form-control'}))
    telefono=CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    facebook=CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    twitter=CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    direccion=CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    latitud=DecimalField(required=True, widget=NumberInput(attrs={'class': 'form-control', 'step':0.00000000000000000001}))
    longitud=DecimalField(required=True, widget=NumberInput(attrs={'class': 'form-control', 'step':0.00000000000000000001}))



class SaleForm(ModelForm):
    class Meta:
        model=Sale
        fields='__all__'

    encabazado=CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    fecha_inicio= DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=DateTimeInput(attrs={
            'class': 'form-control',
        })
    )
    fecha_fin=DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=DateTimeInput(attrs={
            'class': 'form-control',
        })
    )
    descripcion=CharField(required=True, widget=Textarea(attrs={'class':'form-control', 'rows': '3'}))
    tienda=ModelChoiceField(required=True, widget=Select(attrs={'class': 'form-control'}), queryset=Store.objects.all())

