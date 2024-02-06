from django.db import models

# Create your models here.

class Department(models.Model):
    Department_Name = models.CharField(max_length=100,null=False)
    def __str__(self):                                                      # for display in admin page
        return self.Department_Name                                          # for single display

class Role(models.Model):
    Role_Name = models.CharField(max_length=200,null=False)
    def __str__(self):                      
        return self.Role_Name


class Employee(models.Model):
    First_name = models.CharField(max_length=100,null=False)
    Last_name = models.CharField(max_length=100)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)    # defined upper class is inherited here (inherited class must be in upper section )
    Salary = models.IntegerField(default=0)
    Bonus = models.IntegerField(default=0)
    Role = models.ForeignKey(Role,on_delete=models.CASCADE)
    Phone = models.IntegerField(default=0)
    Hiring_date = models.DateField()
    # def __str__(self):                                                                                              
        # return "%s %s %s %s %s %s" %(self.First_name, self.Last_name, self.Salary, self.Bonus, self.Phone, self.Hiring_date)   # for multiple value  