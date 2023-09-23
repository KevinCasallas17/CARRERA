from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Cliente, Inscripcion
from datetime import date, timedelta, datetime

from django.core.exceptions import ValidationError


GENERO = [
    ('M', 'M'),
    ('F', 'F'),
    ('Otro', 'Otro'),
]

SANGRE = [
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

TALLA = [
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
]

class CreacionCliente(UserCreationForm):

    genero = forms.ChoiceField(
        widget= forms.Select(attrs={'class':'campo'}),
        choices=GENERO
    )

    sangre = forms.ChoiceField(
        widget= forms.Select(attrs={'class':'campo'}),
        choices=SANGRE
    )

    talla_camisa = forms.ChoiceField(
        widget= forms.Select(attrs={'class':'campo'}),
        choices=TALLA
    )

    fecha_nacimiento = forms.DateField(
        widget=forms.SelectDateWidget(
            empty_label=("Año", "Mes", "Día"),
            years=range(1990, datetime.now().year + 1)  
        )
    )

    def clean_fecha_nacimiento(self):

        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        fecha_actual = date.today()
        fecha_limite1 = fecha_actual - timedelta(days=1)
        fecha_limite2 = fecha_actual - timedelta(days=2)

        if fecha_nacimiento >= fecha_actual or fecha_nacimiento == fecha_limite1 or fecha_nacimiento == fecha_limite2:
            raise ValidationError("Fecha incorrecta.")
        
        
        return fecha_nacimiento

    class Meta:
        model= Cliente
        fields = ['num_identificacion','nombre','apellido','ciudad','correo','telefono','telefono_emergencia','fecha_nacimiento',
        'genero','pais','eps','sangre','talla_camisa']



CATEGORIAS = [
    ('amateur', 'Amateur'),
    ('intermedio', 'Intermedio'),
    ('avanzado', 'Avanzado'),
]


NIVEL = [
    ('facil', 'Facil'),
    ('medio', 'Medio'),
    ('dificil', 'Dificil'),
]

class InscripcionCarrera(forms.ModelForm):

    categoria = forms.ChoiceField(
        widget= forms.Select(attrs={'class':'campo'}),
        choices=CATEGORIAS
    )

    nivel = forms.ChoiceField(
        widget= forms.Select(attrs={'class':'campo'}),
        choices=NIVEL
    )


    class Meta:

        model= Inscripcion
        exclude=('usuario','fecha_inscripcion')

    
    






