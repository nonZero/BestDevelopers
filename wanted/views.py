import random
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from wanted import forms
from . import models


class AdMixin:
    model = models.Ad
    title = "HELLO WORLD!"


    def get_context_data(self, **kwargs):
        d = super().get_context_data(**kwargs)
        d['foo'] = 1234
        return d


class AdListView(AdMixin, ListView):
    paginate_by = 10


class AdDetailView(AdMixin, DetailView):
    pass


class AdCreateView(AdMixin, CreateView):
    form_class = forms.AdForm


class AdUpdateView(AdMixin, UpdateView):
    form_class = forms.AdForm


class AdDeleteView(AdMixin, DeleteView):
    success_url = reverse_lazy("wanted:list")


class ContactUsView(FormView):
    template_name = "contact_us.html"
    form_class = forms.ContactUsForm
    success_url = reverse_lazy("wanted:list")

    def form_valid(self, form):
        # mail.send_email(form.cleaned_data)
        return super().form_valid(form)
