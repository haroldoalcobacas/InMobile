from django import forms
from .models import Cliente


#cadastrar clients
class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __ini__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for fild_name, field in self.filds.items():
            field.widget.attrs['class'] = 'form-control'