from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.forms import profileUpdateForm,userUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,UpdateView,)
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


@login_required
def Profile(request):
    if request.method== 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated!')
            return redirect('users:profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'profile.html',context)
