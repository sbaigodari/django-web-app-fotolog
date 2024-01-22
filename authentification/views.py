from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from . import forms
from authentification.forms import LoginForm, SignupForm
from django.conf import settings
from authentification.models import User



def login_page(request):

    form = forms.LoginForm()
    message =''

    if request.method == 'POST':

        form = forms.LoginForm(request.POST)
        
        if form.is_valid():

            user =  authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'],)

            if user is not None:

                login(request,user)
     
                return redirect('home')

            else :

                message='Identifiants invalides.'
   
    return render(request,'authentification/login.html',{'form':form,'message':message})


def logout_user(request):

    logout(request)
    return redirect('login')



def signup_page(request):

    form = forms.SignupForm()

    if request.method =='POST':

        form = forms.SignupForm(request.POST)
        
        if form.is_valid():

            user = form.save()

            login(request,user)
            
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request,'authentification/signup.html',{'form':form})


def upload_profil_photo(request):

    form = forms.UploadProfilePhotoForm(instance=request.user)

    if request.method =='POST':

        form = forms.UploadProfilePhotoForm(request.POST,request.FILES,instance=request.user)
        
        if form.is_valid():

            form.save()
            return redirect('home')
        
    return render(request,'authentification/upload_profil_photo.html',{'form':form})
