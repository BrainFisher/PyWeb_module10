from django import forms


class QuoteForm(forms.Form):
    quote_text = forms.CharField(label='Цитата', max_length=500)
    author_name = forms.CharField(label='Автор', max_length=100)
