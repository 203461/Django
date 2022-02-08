from django.urls import path, re_path
from django.conf.urls import include
from loadImage.views import imageView
from loadImage.views import imagenViewDetail

urlpatterns = [
    re_path(r'^archivoImagen/$', imageView.as_view()),
    re_path(r'^archivoImagen/(?P<pk>\d+)$', imagenViewDetail.as_view()),
]