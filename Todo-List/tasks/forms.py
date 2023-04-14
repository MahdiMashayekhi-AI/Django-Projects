from django import forms
from .models import Todo


class UpdateTodoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Update the name of task...'})
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'row': '5', 'placeholder': 'Update the explain of '
                                                                                              'task...'})
    )

    class Meta:
        model = Todo
        fields = 'title', 'body'
