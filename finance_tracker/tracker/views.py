from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm

def home(request):
    return render(request, 'tracker/home.html')

def list_transactions(request):
    expenses = Transaction.objects.filter(type='expense').order_by('-date')
    incomes = Transaction.objects.filter(type='income').order_by('-date')

    grouped_expenses = {}
    for expense in expenses:
        if expense.category.name not in grouped_expenses:
            grouped_expenses[expense.category.name] = []
        grouped_expenses[expense.category.name].append(expense)

    lists = {
        'grouped_expenses': grouped_expenses,
        'incomes': incomes,
    }
    return render(request, 'tracker/list_transactions.html', lists)

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
