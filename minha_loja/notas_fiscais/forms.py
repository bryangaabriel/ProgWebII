from django import forms
from .models import NotaFiscal, ProdutoNotaFiscal
from django.forms.models import inlineformset_factory

class NotaFiscalForm(forms.ModelForm):
    class Meta:
        model = NotaFiscal
        fields = ['numero', 'cliente', 'total']

ProdutoNotaFiscalFormSet = inlineformset_factory(
    NotaFiscal, ProdutoNotaFiscal,
    fields=['produto', 'quantidade', 'preco_unitario'],
    extra=1,
    can_delete=True
)
