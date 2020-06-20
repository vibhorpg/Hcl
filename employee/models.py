from django.db import models


class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=10, null=False, blank=False)
    last_name = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    class Meta:
        db_table = "Employee"
        ordering = ['first_name']
