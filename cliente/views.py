from django.shortcuts import render
from cliente.models import Cliente
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from cliente.models import Cliente


class ClienteIndex(TemplateView):
	template_name = "index.html"

class ClienteList(ListView):
	model = Cliente

class ClienteAdd(CreateView):
	model = Cliente
	fields = ['nome', 'sobrenome', 'dataNascimento']
	success_url = reverse_lazy('client_list')

class ClienteUpdate(UpdateView):
	model = Cliente
	template_name = 'cliente/cliente_update.html'
	fields = "__all__"
	success_url = reverse_lazy('client_list')

class ClienteDelete(DeleteView):
	model = Cliente
	template_name = 'cliente/cliente_delete.html'
	success_url = reverse_lazy('client_list')