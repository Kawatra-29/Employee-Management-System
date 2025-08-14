from django.contrib import admin
from .models import Department, Employee, Attendance, Performance
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Performance)

