from django import forms


class RegistroFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    nacimiento = forms.CharField()
    email = forms.EmailField()


class PrestamoFormulario(forms.Form):

    apellido = forms.CharField(max_length= 40)
    nombre =  forms.CharField(max_length= 40)
    titulo = forms.CharField(max_length= 40)
    fecha_prest = forms.DateField()