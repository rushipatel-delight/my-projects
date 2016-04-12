from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Accounts
from django.db.models import Q

def account(request, account_id):
    account = Accounts.objects.get(id=account_id)
    q = request.GET.get('q', '')
    notes = Note.objects.filter(Q(description__icontains=q) | Q(category__name__icontains=q),
                                account=account_id).order_by('-timestamp').select_related()
    #total = Note.objects.filter(account=account_id).aggregate(Sum('amount'))
    total = account.balance
    return render(request, 'bank/account.html', {"notes": notes, "total": total, "account": account})
