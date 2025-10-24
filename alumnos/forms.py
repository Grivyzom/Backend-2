from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):

    fecha_ingreso = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y', attrs={'placeholder': 'dd-mm-aaaa', 'class': 'form-control'})
    )
    
    class Meta:
          model = Alumno
          fields = ['nombre', 'apellido', 'nota1', 'nota2', 'nota3', 'fecha_ingreso', 'carrera']
          widgets = {
                
                  'nombre': forms.TextInput(attrs={
                        'class': 'form-control'
                  }),
                  'apellido': forms.TextInput(attrs={
                        'class': 'form-control'
                  
                  }),
                  'nota1': forms.NumberInput(attrs={
                        'step': '0.1', 'min': '1.0', 'max': '7.0', 'class': 'form-control'
                        
                  }),
                  'nota2': forms.NumberInput(attrs={
                        'step': '0.1', 'min': '1.0', 'max': '7.0', 'class': 'form-control'
                        
                  }),
                  'nota3': forms.NumberInput(attrs={
                        'step': '0.1', 'min': '1.0', 'max': '7.0', 'class': 'form-control'
                        
                  }),
                  'carrera': forms.Select(attrs={'class': 'form-select'}),
          
          }