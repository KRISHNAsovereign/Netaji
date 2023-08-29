from django import forms
from .models import Subject


class ClassSelectionForm(forms.Form):
    selected_class = forms.ModelChoiceField(queryset=Subject.objects.all())
