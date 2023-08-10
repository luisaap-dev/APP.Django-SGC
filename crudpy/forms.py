from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del cliente'}),
    )

    direccion = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección del cliente'}),
    )

    ciudad = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad del cliente'}),
    )

    pais = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el país del cliente'}),
    )

    telefono = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número de teléfono del cliente'}),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección de correo electrónico del cliente'}),
    )

    foto = forms.ImageField(
    required=False,
    widget=forms.FileInput(attrs={'class': 'form-control-file'}),

)


    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        # Remover cualquier caracter no numérico del número de teléfono
        telefono_limpio = ''.join(filter(str.isdigit, telefono))
        
        if not telefono_limpio.isdigit():
            raise forms.ValidationError("El número de teléfono debe contener solo dígitos.")
        
        return telefono_limpio

    def clean_email(self):
        email = self.cleaned_data['email']
        # Verificar si el email ya está registrado en la base de datos
        if self.instance.pk:
            # Si estamos editando un cliente existente, excluimos este cliente de la búsqueda
            if Cliente.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(
                    "Este correo electrónico ya está registrado.")
        else:
            # Si estamos creando un nuevo cliente, verificamos si el email ya existe
            if Cliente.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "Este correo electrónico ya está registrado.")
        return email
