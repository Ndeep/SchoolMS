from django import forms
from django.contrib.auth.models import User
from student.models import Student
from collegeapp.models import College,Department,Hostel
from collegeapp.utils import DEPARTMENT,Semester,COUNTRIES

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

class StudentForm(forms.ModelForm):
    name=forms.CharField(max_length=50,label='Student Full-Name')
    email=forms.EmailField(max_length=150,label='Option Email-Id')
    mobile=forms.CharField(max_length=10,label='Mobile')
    dob=forms.DateField(label='Date of birth')
    pmobile=forms.CharField(label='Parent Mobile Number',max_length=10)
    semster=forms.ChoiceField(choices=Semester,label='Semster')
    bloodgroup=forms.CharField(max_length=4,label='Blood Group')
    roomnumber=forms.IntegerField(label='Room Number')

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['college'].queryset = College.objects.all()
        self.fields['department'].queryset=Department.objects.all()
        self.fields['hostel'].queryset = Hostel.objects.all()

    class Meta:
        model = Student
        fields='__all__'
