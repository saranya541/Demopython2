from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages,auth
import json

from .models import Person, get_m_strings, get_e_strings,get_k_strings,get_w_strings,get_t_strings
from .forms import PersonForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,'invalid')
            return redirect('login')

    return render(request, 'login.html')

def new(request):
    return render(request,'new.html')


def register(request):
    if request.method =='POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return  redirect('register')
            # elif User.objects.filter(email=email).exists():
            #      messages.info(request, 'invalid')
            #      return redirect('register')
            elif User.objects.filter().exists():
                 messages.info(request, 'invalid ')
                 return redirect('register')

            else:


                user=User.objects.create_user(username=username,password=password)

                user.save();


                return redirect('login')


        else:
            messages.info(request, 'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
def personal_info(request):
    context = {}

    personform = PersonForm()
    context['personform'] = personform

    m_strings = get_m_strings()
    e_strings = get_e_strings()
    k_strings = get_k_strings()
    w_strings = get_w_strings()
    t_strings = get_t_strings()

    json_m_strings = json.dumps(m_strings)
    json_e_strings = json.dumps(e_strings)
    json_k_strings = json.dumps(k_strings)
    json_w_strings = json.dumps(w_strings)
    json_t_strings = json.dumps(t_strings)

    context['json_m_strings'] = json_m_strings
    context['json_e_strings'] = json_e_strings
    context['json_k_strings'] = json_k_strings
    context['json_w_strings'] = json_w_strings
    context['json_t_strings'] = json_t_strings

    if request.method =='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return  redirect('personal_info')
        elif User.objects.filter(email=email).exists():
                 messages.info(request, 'email Taken')
                 # return redirect('personal_info')
        else:


                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                user.save();


                # return redirect('form')




        return redirect('/')

    return render(request, 'personal_info.html', context)
def form(request):
    return render(request,'form.html')


