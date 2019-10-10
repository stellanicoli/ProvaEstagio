from django.conf.urls import url
from .views import*


urlpatterns = [
    url(r'^pet/listar/$', listar_pet, name='listar_pet'),
    url(r'^pet/perfil/(?P<pk>[0-9]+)', perfil_pet, name='perfil_pet'),

]