from django.shortcuts import render, redirect
from .forms import TrademarkForm


# Create your views here.

def home(request):
    form = None
    if request.POST:
        form = TrademarkForm(request.POST, request.FILES)
    else:
        form = TrademarkForm()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return render(request, 'app/thanks.html')
    context = {"form": form}
    return render(request, 'app/index.html', context)
