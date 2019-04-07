from rest.pascal.models import DType, DMathOperation, DClass
from rest_framework import viewsets
from rest.pascal.serializers import (
    TypeSerializer,
    ClassSerializer,
    MathOperationSerializer,
)


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = DType.objects.all()
    serializer_class = TypeSerializer


class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = DClass.objects.all()
    serializer_class = ClassSerializer


class MathOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = DMathOperation.objects.all()
    serializer_class = MathOperationSerializer
