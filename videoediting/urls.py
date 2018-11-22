
from django.urls import path
from . import views


urlpatterns = [
    path('', views.editing, name='editing'),
    path('reason', views.reason, name='reason'),
    path('consq', views.consq, name='consq'),
    path('onemoment', views.onemoment, name='onemoment'),
    path('camera', views.camera, name='camera'),

]
