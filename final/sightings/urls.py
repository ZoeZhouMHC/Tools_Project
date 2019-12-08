from django.urls import include, path
from sightings import views

urlpatterns = [
        path('map/',views.map, name = 'map'),
        path('sightings/', views.sightings, name = 'sightings'),
        path('sightings/add/', views.add, name = 'add'),
        path('sightings/stats/',views.stats, name = 'stats'),
        path('sightings/<squirrel_id>/',views.id, name = 'id'),
]

