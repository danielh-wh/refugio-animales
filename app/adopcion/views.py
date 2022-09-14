from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.adopcion.models import Persona, Solicitud
from django.core.urlresolvers import reverse_lazy
from app.adopcion.forms import PersonaForm, SolicitudForm

#Create your views here.

def index_adopcion(request):
    return HttpResponse("pagina adopcion")

class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'
    paginate_by = 2

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return  HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, request.FILES, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('solicitud_listar')

#funciones
def listarFunciones(request):
    solicitud = Solicitud.objects.all()
    contexto = {'persona': solicitud}
    return render(request, 'adopcion/solicitud_list_funciones.html', contexto)

def eliminarFunciones(request, id_solicitud):
    solicitud = Solicitud.objects.get(id=id_solicitud)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('listar_funciones')
    return render(request,'adopcion/solicitud_delete_func.html', {'persona':solicitud})

def CrearFunciones(request):
    if request.method == 'POST':
        form2 = PersonaForm(request.POST, request.FILES)
        form = SolicitudForm(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return redirect('listar_funciones')
    else:
        form2 = PersonaForm()
        form = SolicitudForm()
    return render(request, 'adopcion/solicitud_form.html', {'form2':form2, 'form':form})

def EditarFunciones(request, id_solicitud):
    solicitud = Solicitud.objects.get(id=id_solicitud)
    persona = Persona.objects.get(id=solicitud.persona_id)
    if request.method == 'GET':
        form = SolicitudForm(instance=solicitud)
        form2 = PersonaForm(instance=persona)
    else:
        form = SolicitudForm(request.POST, instance=solicitud)
        form2 = PersonaForm(request.POST, request.FILES, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
        return redirect('listar_funciones')
    return render(request, 'adopcion/solicitud_form.html', {'solicitud':solicitud, 'form': form, 'form2':form2})

#BUSCADOR
def buscarS(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        soliciitud = Solicitud.objects.filter(persona__nombre__icontains=q)
        return render(request, 'adopcion/resultado_adopcion.html', {'solicitud':soliciitud, 'query':q})
    else:
        return render(request, 'adopcion/resultado_adopcion.html')
