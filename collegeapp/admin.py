from django.contrib import admin
from collegeapp.models import University,College,Department,Subjects,Hostel
# Register your models here.
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_per_page = 10


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display =('name','university','principal','founded')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display =('name','colg','hod')

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name','get_department')

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'warden','hosteltype','college')





