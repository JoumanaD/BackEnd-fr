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
    url(r'^etudiant/$', views.etudiantApi),
    url(r'^etudiant/([0-9]{8})$', views.etudiantApi)
]