from django.contrib import admin
from student.models import Student,Address,StdMarks
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','get_detail')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line','city')

@admin.register(StdMarks)
class StdMarksAdmin(admin.ModelAdmin):
    list_display = ('student','subject','sessionaltext','sessionalMark','internalMark','semster')