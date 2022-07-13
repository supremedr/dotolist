from django.forms import ModelForm
from .models import Lista, Task

class ListaForm(ModelForm):
    class Meta:
        model = Lista
        fields = ['title']

    
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','details','periority']