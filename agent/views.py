from django.shortcuts import render, redirect,get_object_or_404
from django.http  import HttpResponse, HttpResponseRedirect, Http404
import datetime as dt
from .models import User, Building, House
from .forms import CreateUserForm, UploadPicForm, CreateBuildingForm,CreateHouseForm
from django_daraja.mpesa.core import MpesaClient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
     user_type = get_object_or_404(User,pk=request.user.id)
     if not request.user.is_superuser :
           
          user=User.objects.all()
          return render(request, 'pay.html',{'user':user} )
          
     else:
          building=Building.objects.all()
          return render(request, 'home.html',{"building":building})
                 
          

def index(request,phone_number):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    print(phone_number)
    phone_number = phone_number
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'http://4cc0ca50.ngrok.io/'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response.text)

def stk_push_callback(request):
        data = request.body
        # You can do whatever you want with the notification received from MPESA here.

def create_user(request):
     form=CreateUserForm()
     error=False
     if request.method == 'POST':
          print('===================================posted')
          form=CreateUserForm(request.POST)
          if form.is_valid():
               print("===========not")
               if User.objects.filter(email=form.cleaned_data['email']).first():
                    error="User with email already exists"
               else:
                    user = form.save()
                    
               if User.objects.filter(phone_number=form.cleaned_data['phone_number']).first():
                    error="User with this Phone Number already exists"
               else:
                    user = form.save()
               
                    return redirect('home')
     return render(request, "registration.html",{"form":form,"error":error})   



def user_profile(request,id):
     user=User.user_profile(id=id)
     return render(request,'user_profile.html',{"user":user})


def edit_user(request,id):
     form=UploadPicForm
     user=User.user_profile(id=id)
     if request.method == 'POST':
          form=UploadPicForm(request.POST)
          if form.is_valid():
               user = form.save()
               return redirect('view_tenant')
     return render(request,'edit_user.html',{"user":user})


def create_building(request):
     form=CreateBuildingForm()
     error=False
     if request.method == 'POST':
          form=CreateBuildingForm(request.POST)
          if form.is_valid():
               if Building.objects.filter(building_name=form.cleaned_data['building_name']).first():
                    error="Building with similar name already exists"
               else:
                    building = form.save()
                    return redirect('home')
     return render(request, "building_reg.html",{"form":form,"error":error})


def create_house(request):
     form=CreateHouseForm()
     error=False
     if request.method == 'POST':
          form=CreateHouseForm(request.POST)
          if form.is_valid():
               if House.objects.filter(name=form.cleaned_data['name']).first():
                    error="Building with similar name already exists"
               else:
                    house = form.save()
                    return redirect('home')
     return render(request, "house_reg.html",{"form":form,"error":error})

@login_required(login_url='/accounts/login')
def view_houses(request, building_name):
     try:
        this_building = Building.objects.get(building_name=building_name)
     except Building.DoesNotExist:
        raise Http404("Invalid Building Name")
     this_house = House.objects.filter( building=this_building)
     return render(request, 'users.html',{'this_house':this_house,'this_building':this_building})


@login_required(login_url='/accounts/login')
def view_tenant(request, name):
     try:
       user = User.objects.get(house_number=name)
       print(user.image)

     except User.DoesNotExist:
       raise Http404("This house is vacant")
     
     return render(request, 'user_profile.html',locals() )