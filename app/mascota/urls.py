from django.conf.urls import url
from app.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete
from app.mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, buscar

#urls funciones
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', mascota_view, name='mascota_view'),
    # url(r'^listing$', listing, name='listing'),
    url(r'^listar$', mascota_list, name='mascota_lis'),
    url(r'^listarClases', MascotaList.as_view(), name='mascota_list_clases'),
    url(r'^nuevoClases$', MascotaCreate.as_view(), name='mascota_nuevo_clases'),
    url(r'^editarClases/(?P<pk>\d+)$', MascotaUpdate.as_view(), name='mascota_edit_clases'),
    url(r'^eliminarClases/(?P<pk>\d+)$', MascotaDelete.as_view(), name='mascota_eliminar_clases'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_edit'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_delete'),
    url(r'^buscar_mascota/$', buscar, name='buscar_mascota'),
]