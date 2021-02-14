from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Add_Employee #importing models from models.py. 

#Code for viewing the Homepage
def index(request):
    return render(request,'index.html')

#Code for viewing the employee page
def next_employee(request):

    #put all objects from the database into one variable 'all_employee'
    all_employee = Add_Employee.objects.all()

    return render(request, 'employee.html', {'Employees': all_employee})


#Code for viewing the employer page
def next_employer(request):
    return render(request, 'employer.html')


#Code for form submission and redirect back to employer page again
def add_employee_form_submit(request):
    print ("Form is successfully submitted.") #print can only be seen on the terminal, not the browser


    #create local variable for each variable entered using the form
    name = request.POST["name"]
    address = request.POST["address"]
    email = request.POST["email"]
    position = request.POST["position"]
    basic_pay = request.POST["basic_pay"]
    overtime_hours = request.POST["overtime_hours"]
    allowance = request.POST["allowance"]
    days_leave = request.POST["days_leave"]
    other_deductions = request.POST["other_deductions"]

    #assigning the local variable into the database fields
    employee_info = Add_Employee(name = name, address = address, email = email, position = position, basic_pay = basic_pay, overtime_hours = overtime_hours, allowance = allowance, days_leave = days_leave, other_deductions = other_deductions )

    #save the entire stuff
    employee_info.save()

    return render(request, 'employer.html')


def search_employee_form_submit(request):
    if request.method == "POST":
        search_id = request.POST['search_id']
        
        if search_id:
            employee_match = Add_Employee.objects.get( pk = search_id ) #pk is primary key
            employee_match.salary_calculation()

            if employee_match:

                return render (request, 'employee.html', {'Search': employee_match})
            else:
                messages.error(request, 'No results found.')

        else: 
            return HttpResponseRedirect('employee/')

    return render(request, 'employee.html')



