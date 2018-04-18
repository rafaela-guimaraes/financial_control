from django.contrib.auth.models import User
from django import forms
from .models import Entry, Category
from django.utils import timezone


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha',widget=forms.PasswordInput)
    email = forms.CharField(label='Email')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class EntryForm(forms.ModelForm):

    description = forms.CharField(label='Descrição', required=True)
    amount = forms.FloatField(label='Valor', required=True, min_value=0.1)
    entry_date = forms.DateField(label='Data', initial=timezone.now, required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Categoria')

    def __init__(self, *args, **kwargs):
        entry_type = kwargs.pop('entry_type')
        super().__init__(*args, **kwargs)

        if entry_type == 'income':
            self.fields['category'].queryset = Category.objects.filter(entries_type='IN')
        else:
            self.fields['category'].queryset = Category.objects.filter(entries_type='EX')
    
    class Meta:
        model = Entry
        fields = ['category', 'description', 'amount', 'entry_date']

