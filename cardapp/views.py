from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Question

# Create your views here.
def home(request):
    return render(request, 'cardapp/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'cardapp/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'cardapp/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'cardapp/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'cardapp/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'cardapp/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def questionlist(request):
    questions = Question.objects.filter(user=request.user)
    return render(request,'cardapp/questionlist.html',{'questions':questions})



@login_required
def current(request):
    if request.method == 'POST':

        #populate subject list dublicated need refactor
        slist = Question.objects.filter(user=request.user)
        subjectList = []
        
        #distinct query is not supported by sqlite. So we get all records and calculate distinct results 
        for x in slist:
            if x.subject not in subjectList:
                subjectList.append(x.subject)
        
        subject = request.POST['subjectf']
        count = request.POST['countf']
        print(f'subject : {subject}  count: {count}')
        
        #end populate subject list

        questions = Question.objects.filter(user=request.user,subject=subject)[:int(count)] #Question count
            
        questionCount = len(questions)

        return render(request,'cardapp/current.html',{
            'questions':questions,
            'subject':subject,
            'questionCount':questionCount,
            'subjectList':subjectList,
            })
        
    else:
        #populate subject list
        slist = Question.objects.filter(user=request.user)
        subjectList = []
        
        #distinct query is not supported by sqlite. So we get all records and calculate distinct results 
        for x in slist:
            if x.subject not in subjectList:
                subjectList.append(x.subject)

        print(subjectList)
        return render(request,'cardapp/current.html',{'subjectList':subjectList})