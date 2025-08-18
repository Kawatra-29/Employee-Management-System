from django.core.management.base import BaseCommand
from faker import Faker
import random
from myapp.models import Employee, Department, Attendance, Performance  # app name adjust karein

class Command(BaseCommand):
    help = 'Seed the database with fake employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # First create some departments
        departments = []
        dept_names = ['HR', 'Finance', 'Engineering', 'Sales', 'Marketing']

        for name in dept_names:
            dept, created = Department.objects.get_or_create(name=name)
            departments.append(dept)

        self.stdout.write(self.style.SUCCESS(f"Created {len(departments)} departments."))

        # Now create employees
        for _ in range(50):
            department = random.choice(departments)
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=random.randint(6000000000, 9999999999),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=department
            )

            # Attendance
            for _ in range(10):  # 10 random attendance records
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

            # Performance
            for _ in range(3):  # 3 performance reviews
                Performance.objects.create(
                    employee=employee,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with fake data.'))
