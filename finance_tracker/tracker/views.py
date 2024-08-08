from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction, Account
from .forms import TransactionForm, AccountForm

def home(request):
    return render(request, 'tracker/home.html')

def list_transactions(request):
    expenses = Transaction.objects.filter(type='expense').order_by('-date')
    incomes = Transaction.objects.filter(type='income').order_by('-date')
    accounts = Account.objects.all()

    grouped_expenses = {}
    for expense in expenses:
        if expense.category.name not in grouped_expenses:
            grouped_expenses[expense.category.name] = []
        grouped_expenses[expense.category.name].append(expense)

    lists = {
        'grouped_expenses': grouped_expenses,
        'incomes': incomes,
        'accounts': accounts,
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

def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('list_transactions')
    else:
        form = AccountForm()
    return render(request, 'tracker/add_account.html', {'form': form})

def edit_account(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('list_transactions')
    else:
        form = AccountForm(instance=account)
    return render(request, 'tracker/edit_account.html', {'form': form})

def delete_account(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'POST':
        account.delete()
        return redirect('list_transactions')
    return render(request, 'tracker/delete_account.html', {'account': account})
