from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

  ################################# Grupos ######################################

  # Menu de Grupos de la Comunidad
  url(r'^listado_grupos/$', views.grupos_list, name= 'listado_grupos'),

  # Mensjase
  url(r'nuevo_miembro/$', views.new_grupo, name= 'mensaje_grupo'),

  # Agregar un Nuevo Grupo de la Comunidad
  #url(r'^nuevo_grupo/$', vies)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)