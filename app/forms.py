from django import forms

from .models import Add_Employee

class CustomForm(forms.Form):
    '''Form with User, Team and GameCategories'''
    Add_Employee = forms.ModelChoiceField(
        queryset=Add_Employee.objects.all()
    )