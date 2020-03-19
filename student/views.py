from django.shortcuts import render, redirect
from django import forms
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
	return render(request, 'student/login.html', {})



def signup(request):
    if request.method == "POST":     #built-in request.method
        form=SignUpForm(request.POST)    #assign values as in constructor
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')  #cleaned_data removes extraw char added by server.
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request,user)  #make user login of requested user
            return redirect('ungrouped')
    else:
        form=SignUpForm()
    return render(request,'student/signup.html', {'form':form})  #for form.as_p in .html 
