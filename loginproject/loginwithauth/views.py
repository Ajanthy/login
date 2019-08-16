from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from loginwithauth.forms import LoginForm
from loginwithauth.models import admin
from django.views.generic import TemplateView
# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')


def register(request):
        if request.method =='POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        print('user created')

                        username = request.POST['username']
                        email = request.POST['email']
                        psw = request.POST['psw']
                        psw_confirm = request.POST['psw_confirm']

                        if(psw==psw_confirm):

                        #if admin.objects.filter(username==username).exits():

                                #print('user name taken')
                                #return redirect('register/')
                        #else:

                                User = admin(username=username,email=email,password=psw,)
                                User.save()
                                return redirect('register')
                
                else:
                        return redirect('register')
                        print('Password not matching')
        else:
           form = LoginForm()
           return render(request,"registration/register.html",{'form': form})




#.def registerView(request):
    # form = UserCreationForm(request.POST)
        #if form.is_valid():
           # form.save()
            #return redirect('login_url')
    #else:
            #form = UserCreationForm()
   # return render(request,'registration/register.html',{'form': form})
