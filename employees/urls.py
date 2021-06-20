
from django.urls import path
#####
from django.urls import path
from rest_framework import routers
from employees.views import EmployeesViewSet, ReportsEmployeesViewSet
from  rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()
router.register(r'employees', EmployeesViewSet)
router.register(r'reports/employees', ReportsEmployeesViewSet)



app_name = 'employees'

urlpatterns =[
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns+=router.urls