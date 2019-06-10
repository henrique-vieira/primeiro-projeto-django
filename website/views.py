from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from helloworld.models import Funcionario, Curriculo
from website.forms import InsereFuncionarioForm, InsereCurriculoForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")

# LISTA DE CURRICULOS
# ----------------------------------------------

class CurriculoListView(ListView):
    template_name = "website/lista_curriculo.html"
    model = Curriculo
    context_object_name = "curriculos"


# CADASTRAMENTO DE CURRICULOS
# ----------------------------------------------

class CurriculoCreateView(CreateView):
    template_name = "website/cria_curriculo.html"
    model = Curriculo
    form_class = InsereCurriculoForm
    success_url = reverse_lazy("website:lista_curriculo")


# ATUALIZAÇÃO DE CURRICULOS
# ----------------------------------------------

class CurriculoUpdateView(UpdateView):
    template_name = "website/atualiza_curriculo.html"
    model = Curriculo
    fields = '__all__'
    context_object_name = 'curriculo'
    success_url = reverse_lazy("website:lista_curriculo")


# EXCLUSÃO DE CURICULOS
# ----------------------------------------------

class CurriculoDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Curriculo
    context_object_name = 'curriculo'
    success_url = reverse_lazy("website:lista_curriculo")
