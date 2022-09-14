from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from app.mascota.forms import MascotaForm
from app.mascota.models import Mascota
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
# Create your views here.

#VISTAS BASADAS EN FUNCIONES
def index(request):
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota_lis')
    else:
        form = MascotaForm()

    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all()
    paginator = Paginator(mascota, 2)
    page_number = request.GET.get('page', 1)
    if not page_number:
        page_number=1
    try:
        page_number=int(page_number)
    except ValueError:
        page_number=1
    page_obj = paginator.page(page_number)
    contexto = {'mascotas':mascota, 'page_obj':page_obj}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form  = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_lis')
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_lis')
    return render(request,'mascota/mascota_delete.html', {'mascota':mascota})
#FIN VISTAS BASADAS EN FUNCIONES

#VISTAS BASADAS EN CLASES
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list_clases.html'
    paginate_by = 2

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form_clases.html'
    success_url = reverse_lazy('mascota_list_clases')

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form_clases.html'
    success_url = reverse_lazy('mascota_list_clases')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete_clases.html'
    success_url = reverse_lazy('mascota_list_clases')

#PAGINACION
# def listing(request):
#     mascota_lista = Mascota.objects.all()
#     paginator = Paginator(mascota_lista, 2)
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'mascota/mascota_list.html', {'page_obj': page_obj})

#BUSQUEDA
def buscar(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        mascotas = Mascota.objects.filter(nombre__icontains=q) | Mascota.objects.filter(edad_aproximada__icontains=q)
        return render(request, 'mascota/resultado.html', {'mascotas':mascotas, 'query':q})
    else:
        return render(request, 'mascota/resultado.html')