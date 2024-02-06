from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from .models import Department, Role, Employee
from .forms import Employee_form
from django.db.models import Q

# Create your views here.

def home_page(request):
    return render(request,"home_page.html")


def all_emp(request):
    all = Employee.objects.all()
    data = {"all":all}
    return render(request,'all_emp.html',data)


def add_emp(request):
    submit = ''
    if request.method == "POST":
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Phone = int(request.POST['Phone'])
        Salary = int(request.POST['Salary'])
        Bonus = int(request.POST['Bonus'])
        Department_Name = int(request.POST['Department_Name'])
        Role_Name = int(request.POST['Role_Name'])
        Hiring_date = datetime.now()
        Employe = Employee(First_name = First_name, 
                            Last_name = Last_name, 
                            Salary = Salary, 
                            Bonus = Bonus, 
                            Phone = Phone, 
                            Department_id =  Department_Name,
                            Role_id =  Role_Name,
                            Hiring_date = Hiring_date)
        Employe.save()
        submit = "Employee Added Successfuly !"
    data = {"output":submit}
    return render(request,"add_emp.html",data)


def remove_emp(request,emp_id = 0):
    submit = ''
    if emp_id:
        try:
            emp_re = Employee.objects.get(id=emp_id)
            emp_re.delete()
            submit ="Employee removed !"
        except:
            submit="Employee not found !"
    all = Employee.objects.all()
    data = {"all":all,"output":submit}
    return render(request,"remove_emp.html",data)


def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        Department_Name = request.POST['Department_Name']
        Role_Name = request.POST['Role_Name']
        all = Employee.objects.all()
        if name:
            all = all.filter(Q(First_name__icontains = name) | Q(Last_name__icontains = name))
        if Department_Name:
            all = all.filter(Q(Department__Department_Name = Department_Name))
        if Role_Name:
            all = all.filter(Q(Role__Role_Name = Role_Name))
        data = {'all':all}
        return render(request,"all_emp.html",data)
    elif request.method == "GET":
        return render(request,"filter_emp.html")
    else:
        return HttpResponse("Error in programe")