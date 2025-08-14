
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Employee, Department, Attendance, Performance
from .serializers import EmployeeSerializer, DepartmentSerializer, AttendanceSerializer, PerformanceSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes

from django.db.models import Count
from django.db.models.functions import TruncMonth
from .models import Attendance
import calendar



@api_view(['GET'])
@permission_classes([AllowAny])
def dashboard(request):
    return render(request, 'index.html')




class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['department__department_name', 'name']  # Filtering by department name
    ordering_fields = ['date_of_joining', 'name']  # Sorting

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
    


class EmployeesPerDepartmentView(APIView):
    def get(self, request):
        data = (
            Department.objects.annotate(employee_count=Count('employee'))
            .values('name', 'employee_count')
        )
        return Response(data)


class MonthlyAttendanceView(APIView):
    def get(self, request):
        data = (
            Attendance.objects
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(count=Count('id'))
            .order_by('month')
        )
        return Response(data)
    

import json


def attendance_overview(request):
    # Group attendance records by month and status
    data = Attendance.objects.annotate(month=TruncMonth('date')) \
        .values('month', 'status') \
        .annotate(count=Count('id')) \
        .order_by('month')

    # Process data into a structure usable for bar chart
    months = []
    present_counts = []
    absent_counts = []
    late_counts = []

    month_map = {}

    for item in data:
        month_name = item['month'].strftime('%B')
        status = item['status']
        count = item['count']

        if month_name not in month_map:
            month_map[month_name] = {'Present': 0, 'Absent': 0, 'Late': 0}
        
        month_map[month_name][status] = count

    # Final structure for chart
    for month in sorted(month_map.keys(), key=lambda x: list(calendar.month_name).index(x)):
        months.append(month)
        present_counts.append(month_map[month]['Present'])
        absent_counts.append(month_map[month]['Absent'])
        late_counts.append(month_map[month]['Late'])
    
    context = {
        'months': json.dumps(months),  # Convert to JSON string
        'present_counts': json.dumps(present_counts),
        'absent_counts': json.dumps(absent_counts),
        'late_counts': json.dumps(late_counts),
        }

    return render(request, 'attendance_chart.html', context)
