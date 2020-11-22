from django.urls import include, path
#from api import views
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
urlpatterns =[
  path('', include(router.urls)),
  path('projects/all',views.ProjectList),
  path('projects/country/kenya',views.ByCountry),
  path('projects/status/completed',views.ProjectByStatus),
  path('projects/create', views.ProjectCreate)
]
