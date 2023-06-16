from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article anons'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'
            })
        }
