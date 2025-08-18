from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Department: {self.name}"

###############################################################################
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Date of Joining: {self.date_of_joining}, Department: {self.department}"

####################################################################

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late')
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Attendance: {self.employee.name}, Date: {self.date}, Status: {self.status}"

####################################################################

class Performance(models.Model):
    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_date = models.DateField()

    def __str__(self):
        return f"Performance: {self.employee.name}, Review Date: {self.review_date}, Rating: {self.get_rating_display()}"