from django import forms

# Create your models here.

class Employee_form(forms.Form):
    First_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':"form-control"}), label='First_name')
    Department_Name = forms.IntegerField(label='Department_Name')
    Department_Location = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':"form-control"}), label='Department_Location')
    Last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':"form-control"}), label='Last_name')
    Salary = forms.IntegerField(label='Salary')
    Bonus = forms.IntegerField(label='Bonus')
    Role_Name = forms.IntegerField(label='Role_Name')          
    Phone = forms.IntegerField(label='Phone')
    Hiring_date = forms.DateInput()