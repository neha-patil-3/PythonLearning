from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Employee, Position

# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "Crudapp/employee_list.html", context)


@csrf_exempt
def employee_create(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    name = body['name']
    emp_code = body['emp_code']
    mobile_number = body['mobile_number']
    position = Position.objects.get(pk=body['position'])
    employee = Employee(name=name, emp_code=emp_code, mobile_number=mobile_number, position=position)
    employee.save()
    return redirect('/employee/list')


def employee_read(request):
    id = request.GET.get('id')
    employee = Employee.objects.get(pk=id)
    context = {'employee': employee}
    return render(request, "Crudapp/employee_read.html", context)


def employee_delete(request):
    id = request.GET.get('id')
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')


