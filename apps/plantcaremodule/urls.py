from django.urls import path, include

from apps.plantcaremodule import views 


urlpatterns = [
    path('',views.index,name='index'),
]




