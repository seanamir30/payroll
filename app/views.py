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
    latestID1 = Add_Employee.objects.latest('pk')
    latestID = latestID1.pk + 1
    return render(request, 'employer.html',{'latestID':latestID})


#Code for form submission and redirect back to employer page again
def add_employee_form_submit(request):
    #create local variable for each variable entered using the form
    name = request.POST["name"]
    address = request.POST["address"]
    email = request.POST["email"]
    position = request.POST["position"]
    if position == "Doctor/Physician":
        basic_pay1 = 16800
        allowance1 = 400
    elif position == "Parts Repair Section"or position =="Preventive Maintenance Section" or position == "Overhauling Section" or position == "Electrical Section" or position == "Body Building Section" or position == "Machine Shop Section" or position == "Tire Section" or position == "Quick Service Section" or position == "Human Resource" or position == "Time Keeper" or position == "Inventory" or position == "Driver" or position == "Conductor" or position == "Ticket Seller":
        basic_pay1 = 14400
        allowance1 = 400
    elif position == "Engineer" or position == "Accountant" or position == "Foreman":
        basic_pay1 = 1440
        allowance1 = 400
    elif position == "Trainee":
        basic_pay1 = 12888
        allowance1 = 400

    basic_pay = basic_pay1
    allowance = allowance1
   
    #assigning the local variable into the database fields
    employee_info = Add_Employee(name = name, address = address, email = email, position = position, basic_pay = basic_pay,  allowance = allowance)#, days_leave = days_leave, other_deductions = other_deductions,overtime_hours = overtime_hours)

    #save the entire stuff
    employee_info.save()
    messages.success(request, 'Successfully added the employee!')

    return render(request, 'employer.html')


#Code for SEARCH form submission and redirect to employee page if successful; back to home page if unsuccessful
def search_employee_form_submit(request):
    if request.method == "POST":
        search_id = request.POST['search_id']
        
        if search_id:
            try:
                employee_match = Add_Employee.objects.get( pk = search_id ) #pk is primary key
                employee_match.salary_calculation()
                return render (request, 'employee.html', {'search_id': search_id, 'Search': employee_match})

            except Add_Employee.DoesNotExist:
                messages.error(request, 'No results found.')
                
                return render (request, 'index.html')

        else: 
            return render(request, 'index.html')

    return render(request, 'index.html')


#Code for form EDIT submission and redirect back to employer page again
def edit_employee_form_submit(request):
    latestID1 = Add_Employee.objects.latest('pk')
    latestID = latestID1.pk + 1
    if request.method == "POST":
        #create local variable for each variable entered using the form
        days_leave = request.POST["days_leave"]
        other_deductions = request.POST["other_deductions"]
        overtime_hours = request.POST["overtime_hours"]
        edit_employee_id = request.POST['edit_employee_id']

        if edit_employee_id:
            try:
                edit_employee_match = Add_Employee.objects.get(pk = edit_employee_id)#pk is primary key
                edit_employee_match.days_leave = days_leave
                edit_employee_match.other_deductions = other_deductions
                edit_employee_match.overtime_hours = overtime_hours

                edit_employee_match.save()
                messages.success(request, 'Successfully edited the employee!')

                return render(request, 'employer.html',{'latestID':latestID})

            except Add_Employee.DoesNotExist:
                messages.error(request, 'Employee ID does not exist.')
        else: 
            return render(request, 'employer.html',{'latestID':latestID})
            
    return render(request, 'employer.html',{'latestID':latestID})


#Code for form DELETE submission and redirect back to employer page again
def delete_employee_form_submit(request):
    latestID1 = Add_Employee.objects.latest('pk')
    latestID = latestID1.pk + 1
    if request.method == "POST":
        delete_employee_id = request.POST['delete_employee_id']

        if delete_employee_id:
            try:
                delete_employee_match = Add_Employee.objects.get(pk = delete_employee_id)#pk is primary key
                delete_employee_match.delete()

                messages.success(request, 'Successfully deleted the employee!')

                return render(request, 'employer.html',{'latestID':latestID})

            except Add_Employee.DoesNotExist:
                messages.error(request, 'Employee ID does not exist.')

        else: 
            return render(request, 'employer.html',{'latestID':latestID})
            
    return render(request, 'employer.html',{'latestID':latestID})