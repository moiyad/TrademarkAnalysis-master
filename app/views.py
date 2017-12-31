from django.shortcuts import render, redirect
from .forms import TrademarkForm
from .models import Trademark



def RTrademark(request):
    trade = Trademark.objects.all()
    form = None
    if request.POST:
        form = TrademarkForm(request.POST, request.FILES)
    else:
        form = TrademarkForm()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return render(request, 'app/success_trademark.html')
    context = {"form": form, 'trade': trade}
    return render(request, 'app/index.html', context)


def success(request):
    return render(request, 'app/success_trademark.html', )