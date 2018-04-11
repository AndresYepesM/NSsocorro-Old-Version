from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from PIL import ImageFilter
from .models import grupos
from .form import Add_grupos

# Create your views here.

@login_required(login_url= '/login/')
# Mensaje de los Nuevos Grupos
def new_grupos(request):

	return render(request, 'people/grupos/new_grupos.html')

@login_required(login_url= '/login/')
# listado de Los Grupos de la Comunidad
def grupos_list(request):

  context = {'grup': grupos.objects.all().order_by('-id')}
  return render(request, 'people/grupos/list_grupos_menu.html', context)

@login_required(login_url= '/login/')
# Agregar Grupos
def add_grupos(request):

  if request.method == 'POST':
    form = Add_grupos(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('mensaje_grupo'))
  else:
    form = Add_grupos()

  context = {'form' : form}
  return render(request, 'people/grupos/add_grupos.html', context)

@login_required(login_url= '/login/')
# Editar Grupos
def grupos_edit(request, id):

  post = get_object_or_404(grupos, id=id)
  if request.method == 'POST':
    form = Add_grupos(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save(commit= False)
      post.save()
      return redirect('listado_grupos')
  else:
    form = Add_grupos(instance=post)
  context = {'form' : form}
  return render(request, 'people/grupos/edit_grupos.html', context)

@login_required(login_url= '/login/')
# Borrar Grupos
def delete_grupos(request, id):

  post = get_object_or_404(grupos, id=id)
  post.delete()
  return redirect('listado_grupos')