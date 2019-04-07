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
            "id",
        )


class MathOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DMathOperation
        fields = ("name", "type_of_argument", "type_of_value", "description", "id")


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DClass
        fields = ("name", "num_of_methods", "num_of_fields", "id")

