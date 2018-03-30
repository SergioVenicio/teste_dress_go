from django import forms
from core.models import Usuario, Aluguel, Produto


class AluguelForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cliente'
            }
        )
    )
    produto = forms.ModelChoiceField(
        queryset=Produto.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Produto'
            }
        )
    )
    valor = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Valor'
            }
        )
    )
    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cep'
            }
        )
    )

    class Meta:
        model = Aluguel
        fields = ('__all__')


class UsuarioForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha'
            }
        )
    )

    class Meta:
        model = Usuario


class UsuarioAddForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha'
            }
        )
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirmação de senha'
            }
        )
    )

    class Meta:
        model = Usuario
