from django.conf.urls import patterns, include, url
from .views import index, afficher, consulter, auth, ajouter

urlpatterns = patterns('',
   url(r'^$', index, name='index'),
   # RECETTE PART
   url(r'^afficher/$', afficher, name='afficher'),
   url(r'^consulter/(?P<id>\d+)/', consulter, name='consulter'),
   url(r'^ajouter/$', ajouter, name='ajouter'),

   # USER PART
   url(r'^account/auth/$', auth, name='auth'),
)
