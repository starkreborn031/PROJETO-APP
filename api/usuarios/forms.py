from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario

class UsuarioCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'tipo')

    def clean_password2(self):
        senha1 = self.cleaned_data.get('password1')
        senha2 = self.cleaned_data.get('password2')
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("As senhas não coincidem.")
        return senha2

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario

class UsuarioChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'tipo', 'password', 'is_active', 'is_staff', 'is_superuser')
