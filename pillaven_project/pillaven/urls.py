from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('projects/<slug:slug>/', views.pillaven, name='projectpage'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 