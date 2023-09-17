from django import forms
from .models import TodoList


class TodoForm(forms.ModelForm):

    class Meta:
        model = TodoList

        fields = ['title', 'is_done', 'due_date']
        exclude = ['user',]


class UpdateTodoForm(forms.ModelForm):

    class Meta:
        model = TodoList

        fields = ['title', 'is_done', 'due_date']
        exclude = ['user',]
