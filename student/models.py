from django.db import models
from collegeapp.utils import DEPARTMENT,Semester,COUNTRIES
from collegeapp.models import Department,College,Subjects,Hostel
from django.contrib.auth.models import User,AbstractBaseUser
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.core.validators import MaxValueValidator, MinValueValidator,MinLengthValidator,MaxLengthValidator
# Create your models here.



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Student(AbstractBaseUser):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name =models.CharField(max_length=50,verbose_name='Student First Name',null=False,blank=False)
    last_name = models.CharField(max_length=50, verbose_name='Student Last Name', null=False, blank=False)
    email=models.EmailField(max_length=150,verbose_name='Email',null=True,blank=True)
    mobile=models.CharField(max_length=10,verbose_name='Mobile')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    dob=models.DateField(verbose_name='Date of birth',blank=True,null=True)
    pmobile=models.CharField(max_length=10,verbose_name='Parent Mobile Number',blank=True,null=True)
    college=models.ForeignKey(College,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    semester=models.PositiveIntegerField(choices=Semester,verbose_name='Current Semester')
    bloodgroup=models.CharField(max_length=4,null=True,blank=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    roomnumber = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def get_fullname(self):
        return self.first_name+' '+self.last_name

    def get_detail(self):
        return "".join([s.email for s in self.email.objects.all()])

    def email_user(self, subject, message, from_email=None, **kwargs):
        pass


class Address(models.Model):
    address_line=models.CharField(max_length=250,null=False,blank=False)
    city=models.CharField(max_length=20,null=False,blank=False)
    state=models.CharField(max_length=15,null=False,blank=False)
    country=models.CharField(choices=COUNTRIES,max_length=15,default='IN')
    pincode = models.IntegerField(null=False, blank=False,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='StdAddress')

class StdMarks(models.Model):
    sesText=(
        ('1','First Sessional'),
        ('2', 'Second Sessional'),
        ('3', 'Third Sessional'),
        ('4', 'Fourth Sessional'),
    )
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    sessionaltext=models.CharField(choices=sesText,default='1',max_length=1)
    sessionalMark=models.PositiveIntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],default=0)
    internalMark=models.PositiveIntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],default=0)
    semster=models.IntegerField(choices=Semester)



