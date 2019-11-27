from django import forms
from crud.models import Task


class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': DateInput()
        }