from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from student.forms import StudentForm,UserForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
# Create your views here.

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = StudentForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm()
        profile_form = StudentForm()
    return render(request, 'student/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
