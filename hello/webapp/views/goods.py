from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.http import urlencode
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import Goodform, GoodDeleteForm, SimpleSearchForm
from webapp.models import Goods
from django.urls import reverse_lazy
from django.db.models import Q



class IndexView_good(ListView):
    model = Goods
    template_name = 'Good/index.html'
    context_object_name = 'goods'
    paginate_by = 3
    paginate_orphans = 1


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, object_list = None, **kwargs):
        context = super().get_context_data(object_list= object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)  | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by('category', 'name')

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None




class Good_more(DetailView):
    model = Goods
    template_name = 'Good/good_more.html'



class Good_add(LoginRequiredMixin, CreateView):
    template_name = 'Good/good_add.html'
    model = Goods
    form_class = Goodform

    def get_success_url(self):
        return reverse('see_good', kwargs = {'pk': self.object.pk})


class Good_change(LoginRequiredMixin, UpdateView):
    model = Goods
    template_name = 'Good/change_good.html'
    form_class = Goodform
    context_object_name = 'goods'

    def get_success_url(self):
        return reverse('see_good', kwargs={'pk': self.object.pk})




class Good_delete(LoginRequiredMixin, DeleteView):
    template_name = 'Good/good_del.html'
    model = Goods
    context_object_name = 'goods'
    success_url = reverse_lazy('main_page')
