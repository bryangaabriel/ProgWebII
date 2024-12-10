from django.shortcuts import render, get_object_or_404, redirect
from .models import NotaFiscal, ProdutoNotaFiscal
from produtos.models import Produto
from clientes.models import Cliente
from .forms import NotaFiscalForm, ProdutoNotaFiscalFormSet

def lista_notas_fiscais(request):
    notas = NotaFiscal.objects.all()
    return render(request, 'notas_fiscais/lista_notas_fiscais.html', {'notas': notas})

def adicionar_nota_fiscal(request):
    if request.method == 'POST':
        form = NotaFiscalForm(request.POST)
        formset = ProdutoNotaFiscalFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            nota = form.save()
            formset.instance = nota
            formset.save()
            return redirect('lista_notas_fiscais')
    else:
        form = NotaFiscalForm()
        formset = ProdutoNotaFiscalFormSet()
    return render(request, 'notas_fiscais/form_nota_fiscal.html', {'form': form, 'formset': formset})

def editar_nota_fiscal(request, id):
    nota = get_object_or_404(NotaFiscal, id=id)
    if request.method == 'POST':
        form = NotaFiscalForm(request.POST, instance=nota)
        formset = ProdutoNotaFiscalFormSet(request.POST, instance=nota)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('lista_notas_fiscais')
    else:
        form = NotaFiscalForm(instance=nota)
        formset = ProdutoNotaFiscalFormSet(instance=nota)
    return render(request, 'notas_fiscais/form_nota_fiscal.html', {'form': form, 'formset': formset})

def excluir_nota_fiscal(request, id):
    nota = get_object_or_404(NotaFiscal, id=id)
    if request.method == 'POST':
        nota.delete()
        return redirect('lista_notas_fiscais')
    return render(request, 'notas_fiscais/confirmar_exclusao.html', {'nota': nota})

def detalhes_nota_fiscal(request, id):
    nota = get_object_or_404(NotaFiscal, id=id)
    return render(request, 'notas_fiscais/detalhes_nota_fiscal.html', {'nota': nota})
