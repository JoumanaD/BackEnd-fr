from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

"""
router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
"""
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [ 
    url(r'^etudiant/$', views.etudiant_list),
    url(r'^etudiant/(?P<pk>[0-9]{8})$', views.etudiant_detail),
    url(r'^fiche/$', views.fiche_list),
    url(r'^fiche/(?P<pk>[0-9]+)$', views.fiche_detail),
    url(r'^adresse/$', views.adresse_list),
    url(r'^adresse/(?P<pk>[0-9]+)$', views.adresse_detail),
    url(r'^etablissement/$', views.etablissement_list),
    url(r'^etablissement/(?P<pk>[0-9]+)$', views.etablissement_detail),
    url(r'^rhservice/$', views.rhservice_list),
    url(r'^rhservice/(?P<pk>[0-9]+)$', views.rhservice_detail),
    url(r'^accueilservice/$', views.accueilservice_list),
    url(r'^accueilservice/(?P<pk>[0-9]+)$', views.accueilservice_detail)
]