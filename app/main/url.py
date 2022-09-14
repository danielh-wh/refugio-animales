from django.conf.urls import url
from app.main.views import Inicio

urlpatterns = [
    url(r'^$', Inicio, name='Inicio'),
]