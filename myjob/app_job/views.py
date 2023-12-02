from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementsForm

def index(request):
    advertisement = Advertisement.objects.all()
    context = {'advertisement': advertisement}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

def advertisement_post(request):
    form = AdvertisementsForm()
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisement(**form.cleaned_data)
            advertisements.user = request.user
            advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)
