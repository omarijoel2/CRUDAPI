from django.urls import include, path
#from api import views
from rest_framework import routers
from . import views

router= routers.DefaultRouter()
urlpatterns =[
  path('', include(router.urls)),
  path('/projects/all', views.get_projects),
  path('/projects/country/kenya', views.getByCountry),
  path('/projects/status/completed', views.getProjectByStatus),
  #path('deletebook/<int:book_id>', views.delete_book)
]
