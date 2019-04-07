import sys

from rest.pascal.models import DType, DMathOperation, DClass
from rest_framework import serializers


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DType
        fields = (
            "name",
            "min_value",
            "max_value",
            "format_of_value",
            "size",
            "description",
        )


class MathOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DMathOperation
        fields = ("name", "type_of_argument", "type_of_value", "description")


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DClass
        fields = ("name", "number_of_methods", "number_of_properties")

