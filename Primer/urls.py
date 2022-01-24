from django.urls import path, re_path
from django.conf.urls import include


from Primer.views import PrimerTablaList

urlpatterns = [
    re_path(r'^lista/$', PrimerTablaList.as_view()),    
]