import random
from django.shortcuts import render, redirect

from wanted import forms
from . import models

# ad = models.Ad.objects.get(id=12)



def ad_list(request):

    ads = models.Ad.objects.all()

    return render(request, "ad_list.html", {
        'object_list': ads,
    })


def ad_detail(request, id):
    ad = models.Ad.objects.get(id=int(id))

    return render(request, "ad_detail.html", {
        'object': ad,
    })


def ad_add(request):
    if request.method == "POST":
        form = forms.AdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("wanted:list")
    else:
        form = forms.AdForm()
    return render(request, "contact_us.html", {
        'form': form,
    })

def contact_us(request):
    if request.method == "POST":
        form = forms.ContactUsForm(request.POST)
        if form.is_valid():
            # do something...
            return redirect("wanted:list")
    else:
        form = forms.ContactUsForm()
    return render(request, "contact_us.html", {
        'form': form,
    })
