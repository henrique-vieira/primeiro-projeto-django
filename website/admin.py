from django.contrib import admin

from helloworld.models import Funcionario
from helloworld.models import Curriculo

admin.site.register(Funcionario)
admin.site.register(Curriculo)
