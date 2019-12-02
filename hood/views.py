from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Neighbourhood, User, Business, Category, News, Service
from .forms import *
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Neighbourhood, User, Business, Category, News, Service
from .forms import *
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def index(request):
    '''
    View function to user registration page
    '''
    current_user=request.user
    user=User.objects.filter(name = current_user).all()

    if user:
        return redirect('home')

    else:
        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save(commit=False)
                user.name = current_user
                user.save()
                send_welcome_email(user.name, user.email_address)
            return redirect('profile')
        else:
            form = UserForm()

    return render(request, 'index.html',{"form":form})

@login_required(login_url="/accounts/login/")
def home(request):
    '''
    View function to landing page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id
    news = News.objects.filter(neighbourhood_id = neighbourhood).all()
    businesses = Business.objects.filter(neighbourhood_id = neighbourhood).all()
    services = Service.objects.filter(neighbourhood_id = neighbourhood).all()
    gossips = News.objects.filter(neighbourhood_id = neighbourhood, category__category_name = 'gossip').all()
    announcements = News.objects.filter(neighbourhood_id = neighbourhood, category__category_name = 'general').all()

    return render(request, 'home.html', {"current_user":current_user, "main_user":user, "businesses":businesses, "services":services, "neighbourhood":neighbourhood, "news":news, "gossips":gossips, "announcements":announcements})

@login_required(login_url="/accounts/login/")
def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
        return redirect('profile')
    else:
        categoryform = CategoryForm()

    return redirect('profile')

@login_required(login_url='/accounts/login/')
def search(request):
    if 'search_name' in request.GET and request.GET['search_name']:
        searched=request.GET.get("search_name")
        current_user=request.user
        user = User.objects.get(name = current_user)
        neighbourhood = user.neighbourhood_id
        news = News.objects.filter(neighbourhood_id = neighbourhood, title__icontains = searched).all()
        businesses = Business.objects.filter(neighbourhood_id = neighbourhood, name__icontains = searched).all()
        services = Service.objects.filter(neighbourhood_id = neighbourhood, title__icontains = searched).all()
        message=f'{searched}'

        return render(request,'search.html',{"message":message,"businesses":businesses,"services":services,"news":news,"name":searched, "neighbourhood":neighbourhood, "main_user":user})
    else:
        message="You did not search anything please input somrthing to search"
        return render(request,"search.html",{"message":message})

@login_required(login_url="/accounts/login/")
def profile(request):
    '''
    View function for profile page
    '''
    title = request.user.username
    try:
        current_user=request.user
        profile=User.objects.get(name = current_user)
        neighbourhood = profile.neighbourhood_id
        news = News.objects.filter(user = profile).all()

        if request.method == 'POST':
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                news = form.save(commit=False)
                news.user = profile
                news.neighbourhood_id = neighbourhood
                news.save()
            return redirect('profile')
        else:
            form = NewsForm()

    except Exception as e:
        raise Http404()

    categoryform = CategoryForm()

    return render(request,"profile.html",{'profile':profile, "title":title, "form":form, "news":news, "categoryform": categoryform, "main_user":profile})

@login_required(login_url="/accounts/login/")
def change(request):
    '''
    View function for profile page
    '''
    title = request.user.username
    try:
        current_user=request.user
        olduser=User.objects.get(name = current_user)

        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                User.objects.filter(name = current_user).all().delete()
                newuser = form.save(commit=False)
                newuser.name = current_user
                newuser.save()
            return redirect('profile')
        else:
            form = UserForm()

    except Exception as e:
        raise Http404()

    return render(request, "change.html", {"form":form})

@login_required(login_url="/accounts/login/")
def services(request):
    '''
    View function for services page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id
    services = Service.objects.filter(neighbourhood_id = neighbourhood).all()

    return render(request, 'services.html', {'current_user':current_user, "main_user":user, "services":services})

def business(request):
    '''
    View function for business page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id
    businesses = Business.objects.filter(neighbourhood_id = neighbourhood).all()

    return render(request, 'business.html', {'current_user':current_user, "main_user":user, "businesses":businesses})

@login_required(login_url="/accounts/login/")
def about(request):
    '''
    View function for about page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)

    return render(request, 'about.html', {"main_user":user})

@login_required(login_url="/accounts/login/")
def newbusiness(request):
    '''
    View function for business form page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = user
            business.neighbourhood_id = neighbourhood
            business.save()
        return redirect('user_admin')
    else:
        businessform = BusinessForm()

    return redirect('user_admin')

@login_required(login_url="/accounts/login/")
def newservice(request):
    '''
    View function for new service page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.neighbourhood_id = neighbourhood
            service.save()
        return redirect('user_admin')
    else:
        serviceform = ServiceForm()

    return render('user_admin')

@login_required(login_url="/accounts/login/")
def newneighbourhood(request):
    '''
    View function for new service page
    '''
    current_user=request.user
    admin=User.objects.get(name = current_user)
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id

    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = current_user
            neighbourhood.occupants_count = 1
            neighbourhood.save()
        return redirect('user_admin')
    else:
        neighbourhoodform = NeighbourhoodForm()

    return render('user_admin')

@login_required(login_url="/accounts/login/")
def user_admin(request):
    '''
    View function for admin Page
    '''
    current_user=request.user
    user = User.objects.get(name = current_user)
    neighbourhood = user.neighbourhood_id
    news = News.objects.filter(neighbourhood_id = neighbourhood).all()
    businesses = Business.objects.filter(neighbourhood_id = neighbourhood).all()
    services = Service.objects.filter(neighbourhood_id = neighbourhood).all()
    occupants = User.objects.filter(neighbourhood_id = neighbourhood).all()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = user
            news.neighbourhood_id = neighbourhood
            news.save()
        return redirect('user_admin')
    else:
        form = NewsForm()

    businessform = BusinessForm()
    categoryform = CategoryForm()
    serviceform = ServiceForm()
    neighbourhoodform = NeighbourhoodForm()

    return render(request, 'admin.html', {'news':news,'current_user':current_user, "main_user":user, "businesses":businesses, "services":services, "form":form, "neighbourhoodform":neighbourhoodform, "businessform":businessform, "categoryform":categoryform, "serviceform":serviceform, "occupants":occupants})
