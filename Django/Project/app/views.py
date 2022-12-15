from django.shortcuts import render
from .models import Shop
from django.utils import timezone
from django.shortcuts import redirect
from .forms import ShopForm

def app_list(request):
    apps = Shop.objects.all()
    context = {
        'apps':apps
    }
    return render(request, 'app_list.html', context)

def app_create(request):
    form = ShopForm()
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/app/')
    context = {
        'form': form
    }
    return render(request, 'app_create.html', context)

def app_product(request, pk):
    app = Shop.objects.get(id=pk)
    context = {
        'app': app
    }
    return render(request, 'app_product.html', context)

def app_update(request, pk):
    app = Shop.objects.get(id=pk)
    form = ShopForm(instance=app)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
        return redirect('/app/')
    context = {
        'form': form
    }
    return render(request, 'app_update.html', context)

def app_delete(request, pk):
    app = Shop.objects.get(id=pk)
    app.delete()
    return redirect('/app/')

