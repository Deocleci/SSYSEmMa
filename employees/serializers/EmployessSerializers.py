from rest_framework import serializers

from employees.models import Employees



class EmployessSerializers(serializers.ModelSerializer):

    class Meta:
        model= Employees
        fields = '__all__'