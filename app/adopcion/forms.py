from django import forms
from app.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
            'imagen_perfil',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
            'imagen_perfil': 'Imagen de perfil'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'domicilio': forms.Textarea(attrs={'class': 'form-control'}),
            #'imagen_perfil': forms.ImageField(),
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]

        labels = {
            'numero_mascotas': 'Numero de mascotas',
            'razones': 'Razones',
        }

        widgets = {
            'numero_mascotas':forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'razones':forms.Textarea(attrs={'class':'form-control'})
        }