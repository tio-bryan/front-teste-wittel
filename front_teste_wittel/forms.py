from django import forms


class ClienteForm(forms.Form):
    nome = forms.CharField(max_length=150, help_text='Até 150 caracteres.')
    cpf = forms.CharField(
        max_length=11,
        help_text='11 dígitos (Sem pontuação).')
    data_nascimento = forms.DateField()
    data_cadastro = forms.DateTimeField()
    renda_familiar = forms.DecimalField(max_digits=65, decimal_places=2, help_text='Até 150 caracteres.')