from rest.pascal.models import DType, DMathOperation, DClass
from rest_framework import generics
from rest.pascal.serializers import (
    TypeSerializer,
    ClassSerializer,
    MathOperationSerializer,
)


class TypeViewList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = DType.objects.all()
    serializer_class = TypeSerializer


class TypeViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DType.objects.all()
    serializer_class = TypeSerializer


class ClassViewList(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = DClass.objects.all()
    serializer_class = ClassSerializer


class ClassViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DClass.objects.all()
    serializer_class = ClassSerializer


class MathOperationViewList(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = DMathOperation.objects.all()
    serializer_class = MathOperationSerializer


class MathOperationViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DMathOperation.objects.all()
    serializer_class = MathOperationSerializer
