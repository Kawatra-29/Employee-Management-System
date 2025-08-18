from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, AttendanceViewSet, PerformanceViewSet
from .views import EmployeesPerDepartmentView
from . import views

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employees-per-department/', EmployeesPerDepartmentView.as_view(), name='employees-per-department'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('attendance-chart/', views.attendance_overview, name='attendance-chart'),
]

