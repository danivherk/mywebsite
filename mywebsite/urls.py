from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from services import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('videoediting/', include('videoediting.urls')),
    path('mediaconsulting/', include('mediaconsulting.urls')),
    path('design/', include('design.urls')),
    path('audio/', include('audio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
