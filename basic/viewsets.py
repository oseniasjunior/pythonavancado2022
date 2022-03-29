from rest_framework import viewsets
from basic import models, serializers


# Métodos HTTP
# POST - CADASTRAR {"name": "MATEMATICA"}
# PUT - ATUALIZAR
# PATCH - ATUALIZAR PARCIAL
# DELETE - DELETAR
# GET - CONSULTAR
class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()  # SELECT * FROM course
    serializer_class = serializers.CourseSerializer
