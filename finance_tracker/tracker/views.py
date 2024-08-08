from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm

def home(request):
    return render(request, 'tracker/home.html')

def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'tracker/list_transactions.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_transactions')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_transaction.html', {'form': form})

def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('list_transactions')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'tracker/edit_transaction.html', {'form': form})

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('list_transactions')
    return render(request, 'tracker/delete_transaction.html', {'transaction': transaction})
