from django import forms
from app.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'genero',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]

        labels = {
            'nombre': 'Nombre',
            'genero': 'Genero',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacuna',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'genero': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }