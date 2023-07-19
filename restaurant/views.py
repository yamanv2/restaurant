from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'restaurant/home.html')

def dashboard(request):
    return render(request, 'restaurant/dashboard.html')

@login_required(login_url='Login')
def menu(request):
    menu_item = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'menu_item':menu_item})

@login_required(login_url='Login')
def order(request):
    order = Purchase.objects.all()
    return render(request, 'restaurant/order.html', {'order':order})

@login_required(login_url='Login')
def recipe_requirement(request):
    recipe_requirement = RecipeRequirement.objects.all()
    return render(request, 'restaurant/recipe_requirement.html', {'recipe_requirement':recipe_requirement})

@login_required(login_url='Login')
def manageOrder(request):
    form = OrderForm()
    if request.method == 'POST':

        # print('Printing POST', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order')
        

    context = {'form':form}
    return render(request, "restaurant/order_form.html", context)


@login_required(login_url='Login')
def updateOrder(request,pk):
    order=Purchase.objects.get(id=pk)
    form=OrderForm(instance=order)

    if request.method == 'POST':

        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/order')
        
    context={'form':form}
    return render(request, "restaurant/order_form.html", context)


@login_required(login_url='Login')
def deleteOrder(request,pk):
    order=Purchase.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/order')

    context={'item':order}
    return render(request, 'restaurant/delete.html', context)


# login & sign up 

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username Or Password is incorrect.')
                
        context ={}
        return render(request, "restaurant/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('Login')



def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account is created for ' + user)
                return redirect('Login')
        context ={"form":form}
        return render(request, "restaurant/signup.html", context)