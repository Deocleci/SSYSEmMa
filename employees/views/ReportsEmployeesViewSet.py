from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, generics,  mixins, status
from employees.models import Employees
from rest_framework.response import Response
from employees.serializers import EmployessSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ReportsEmployeesViewSet(viewsets.ViewSet):
    queryset = Employees.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    @action(methods=['get'], detail=False)
    def age(self, pk=None):
        older = self.queryset.order_by('birth_date')[0]
        younger = self.queryset.order_by('-birth_date')[0]
        return_data = {
            'younger': EmployessSerializers(younger).data,
            'older': EmployessSerializers(older).data,
            'average': Employees().average_age()
        }
        return Response(return_data)
    @action(methods=['get'], detail=False)
    def salary(self, request, pk=None):
        lowest = self.queryset.order_by('salary')[0]
        highest = self.queryset.order_by('-salary')[0]
        return_salary = {
            'lowest': EmployessSerializers(lowest).data,
            'highest': EmployessSerializers(highest).data,
            'average': Employees().report_salary()
        }
        return Response(return_salary)