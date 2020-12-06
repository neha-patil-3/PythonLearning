from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'mobile_number', 'position', 'emp_code')
        labels = {
            'name': 'Full Name',
            'emp_code': 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
