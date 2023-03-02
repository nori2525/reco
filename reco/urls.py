from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reco'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('single/', views.single, name='single')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)