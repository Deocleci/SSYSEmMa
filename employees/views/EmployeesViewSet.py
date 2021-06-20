from rest_framework.viewsets import  ModelViewSet
from employees.serializers import EmployessSerializers
from employees.models import Employees
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class EmployeesViewSet(ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployessSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']