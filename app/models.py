#define database in this file
from django.db import models 

#Class in model.py acts as a table in database
class Add_Employee(models.Model): 
    name = models.CharField (max_length = 150, default = '', null = False)
    position = models.CharField (max_length = 150, default = '', null = False)
    email = models.EmailField (max_length = 150, default = '', null = False)
    address = models.CharField (max_length = 500, default = '', null = False)
    basic_pay = models.FloatField(default=None) 
    overtime_hours = models.IntegerField(default=None)
    allowance = models.FloatField(default=None)
    days_leave = models.IntegerField(default=None)
    other_deductions = models.FloatField(default=None)


    #Django admin page; the table will show the name
    def __str__(self):
        return '{}{}'.format(self.name, self.position, self.email, self.address)

    def salary_calculation(self):

        #Earnings
        self.overtime_hours_pay = self.overtime_hours * 64 

        self.gross_income = self.basic_pay + self.overtime_hours + self.allowance

        #Deductions
        self.days_leave = self.days_leave * 512
        self.pagibig = self.basic_pay * 0.01
        self.gsis = self.basic_pay * 0.09
        self.withholdingtax = self.basic_pay * 0.15
        self.philhealth = self.basic_pay * 0.0275 / 2

        self.total_deductions = self.days_leave + self.pagibig + self.gsis + self.withholdingtax + self.philhealth

        #Net Pay
        self.net_pay = self.gross_income - self.total_deductions


        return (self)


        