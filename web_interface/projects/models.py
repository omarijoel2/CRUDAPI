from django.db import models
from django_countries.fields import CountryField
#from enum import Enum
#from django_enum_choices.fields import EnumChoiceField

# Create your models here.


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    ProjectRef=models.CharField(max_length=20,help_text='Enter field documentation')
    ProjectTitle=models.TextField()
    Country=models.ForeignKey('Country',on_delete=models.CASCADE, verbose_name = "Country")
    ImplementingOffice=models.ForeignKey('Office', on_delete=models.CASCADE)
    DateFromGcf= models.DateField()
    StartDate=models.DateField()
    EndDate=models.DateField()
    Disbursement=models.IntegerField()
    GrantAmount= models.IntegerField()
    #Readiness= models.ForeignKey('Readiness', on_delete=models.CASCADE)
    TypeOfReadiness= models.ForeignKey('Readiness', on_delete=models.CASCADE)
    Status= models.CharField(max_length=20)

#class Grants(models.Model):
    #GrantId= models.AutoField(primary_key=True)
    #Amount=models.IntegerField()
    #project_id=models.ForeignKey('Projects',on_delete=models.CASCADE)




class Readiness(models.Model):
    Id=models.AutoField(primary_key=True)

    TypeOfReadiness=models.CharField(max_length=225, verbose_name = "Type of Readiness")



class Country(models.Model):
    Country_Id= models.AutoField(primary_key=True)
    Country=CountryField(verbose_name = "Country Name")



class Office(models.Model):
    Id=models.AutoField(primary_key=True)
    ImpelementingOffice=models.CharField(max_length=225,verbose_name = "Impelementing Office")

class Disbursement(models.Model):
    id= models.AutoField(primary_key=True)
    Amount=models.IntegerField()
    project_Id= models.ForeignKey('Projects',on_delete=models.CASCADE )
