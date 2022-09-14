from django.conf.urls import url
from app.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete, CrearFunciones, listarFunciones, eliminarFunciones, EditarFunciones, buscarS

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', index_adopcion),
    url(r'^Solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^Solicitud/crear$', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^Solicitud/actualizar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitud_actualizar'),
    url(r'^Solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='solicitud_eliminar'),
    url(r'^Solicitud/crear_funciones$', CrearFunciones, name='crear_funciones'),
    url(r'^Solicitud/listar_funciones$', listarFunciones, name='listar_funciones'),
    url(r'^Solicitud/eliminar_funciones/(?P<id_solicitud>\d+)/$', eliminarFunciones, name='eliminar_funciones'),
    url(r'^Solicitud/editar_funciones/(?P<id_solicitud>\d+)/$', EditarFunciones, name='editar_funciones'),
    url(r'^buscarS$', buscarS, name='buscarS')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)