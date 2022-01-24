from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from Primer.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields= ('nombre','edad')