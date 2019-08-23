from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from loginwithauth.forms import LoginForm
from loginwithauth.models import admin
from django.views.generic import TemplateView
from django import forms
from django.contrib.auth import authenticate, login

# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')



def login(request):
        if request.method =='POST':


                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        # Redirect to a success page.
                        ...
                else:
                        # Return an 'invalid login' error message.
                        ...


        
        else:


                return render(request,"registration/login.html")


def register(request):
        if request.method =='POST':
                form1 = LoginForm(request.POST)
                if form1.is_valid():


                        username = form1.cleaned_data['username']
                        email = form1.cleaned_data['email']
                        psw = form1.cleaned_data['password']
                        psw_confirm = form1.cleaned_data['confirm_password']


                        #if(psw==psw_confirm):

                               # A = admin.objects.get(username)
                                #if not (admin.objects.filter(username=username).exists()):

                                        
                        User = admin(username=username,email=email,password=psw,)
                        User.save()
                        return render(request,"registration/register.html",{'form': form1})

                                        #return redirect('register/')
                                
                                #else:
                                      # raise forms.ValidationError('Looks like a username with that email or password already exists')
                                       #return render(request,"registration/register.html",{'form': form})
                                       
                        

                
                else:
                        return render(request,"registration/register.html",{'form': form1})

                        #print('Password not matching')
        else:
           form1 = LoginForm()
           return render(request,"registration/register.html",{'form': form1})




#.def registerView(request):
    # form = UserCreationForm(request.POST)
        #if form.is_valid():
           # form.save()
            #return redirect('login_url')
    #else:
            #form = UserCreationForm()
   # return render(request,'registration/register.html',{'form': form})
