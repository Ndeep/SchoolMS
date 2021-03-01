from django.db import models
from collegeapp.utils import DEPARTMENT
from django.core.validators import MaxLengthValidator,MinValueValidator

class University(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False,unique=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class College(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    university=models.ForeignKey(University,on_delete=models.CASCADE,related_name='collegerel')
    principal=models.CharField(max_length=20,verbose_name='College Principal',null=True,blank=True)
    founded=models.IntegerField(null=True,blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    hod=models.CharField(max_length=20,verbose_name='Head of the Department')
    colg=models.ForeignKey(College,on_delete=models.CASCADE,verbose_name='College')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Subjects(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    department=models.ManyToManyField(Department)
    deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_department(self):
        return ",\n".join([p.name for p in self.department.all()])

class Hostel(models.Model):
    HostelType=\
        (
            ('Boys','Boys Hostel'),
            ('Girls', 'Girls Hostel'),
    )
    name=models.CharField(max_length=150,verbose_name='Hostel Name')
    college=models.ForeignKey(College,on_delete=models.SET_NULL,null=True)
    warden=models.CharField(max_length=150,verbose_name='Hostel Warden Name')
    phone=models.CharField(max_length=12,verbose_name='Hostel Office Number')
    hosteltype=models.CharField(choices=HostelType,max_length=5)
    bed=models.PositiveIntegerField(verbose_name='Capacity',default=0)
    founded=models.PositiveIntegerField(validators=[MinValueValidator(4)])

    def get_college(self):
        return "\n".join([c.name for c in self.college.all()])






