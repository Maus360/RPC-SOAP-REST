from django.db import models

# Create your models here.


class DType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    min_value = models.CharField(max_length=50)
    max_value = models.CharField(max_length=50)
    format_of_value = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"<User({self.name}, {self.min_value}, {self.max_value}, {self.size}, {self.format_of_value}, {self.description})>"


class DMathOperation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    type_of_argument = models.CharField(max_length=50)
    type_of_value = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"<MathOperation({self.name}, {self.type_of_argument}, {self.type_of_value}, {self.description})>"


class DClass(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    num_of_methods = models.IntegerField()
    num_of_fields = models.IntegerField()

    def __str__(self):
        return f"<Class({self.name}, {self.num_of_methods}, {self.num_of_fields})>"
