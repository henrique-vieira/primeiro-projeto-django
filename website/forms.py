from helloworld.models import Funcionario, Curriculo
from input_mask.widgets import InputMask
from django import forms
from input_mask.contrib.localflavor.br.widgets import BRCPFInput



# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]

class InsereCurriculoForm(forms.ModelForm):

            class Meta:
                # Modelo base
                model = Curriculo

                # Campos que estarão no form
                fields = [
                    'nome',
                    'cpf',
                    'TelCelular',
                    'TelFixo',
                    'sexo',
                    'estado_civil',
                    'email',
                    'idade',
                    'remuneracao',
                    'login',
                    'rua',
                    'numero',
                    'bairro',
                    'cidade',
                    'estado',
                    'cep',
                    'curriculo',
                    'descricao',
                    'criadoData',
                    'status'
                ]

class  MyCustomInput(InputMask):
  mask_cpf = {'cpf': '000.000.000-00'}

