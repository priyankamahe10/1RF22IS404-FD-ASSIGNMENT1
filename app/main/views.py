from django.shortcuts import render
from django.http import HttpResponse
from .forms import inputform,inputform1
from .models import Student,Customer

def home(request):
    return HttpResponse("Hello world")

# list_of_tuples=list(zip(list1,list2)) combining two list

# Factorial for number in range(3,8) 
def fact(request):
    fact_list = []
    for num in range(3, 8):
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        fact_list.append((num, fact))
    return render(request, 'squrae.html', {'fact_list':fact_list})

#square and factorial  of number  5                                    
def hello(request):
    n=5
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    sq=5*5   
    return render(request,'index.html',{'param1':fact1,'param2':n,'sq':sq})   
 
#Take a  word,FOR example “EAT”, Display all 6 combinations 
def get_possibilities(s):
    if len(s) == 1:
        return [s]
    possibilities = []
    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i+1:]
        for p in get_possibilities(remaining_str):
            possibilities.append(char + p)
    return possibilities

def index(request):
    if request.method == 'POST':
        input_string = request.POST.get('input_string')
        permutations = get_possibilities(input_string)
        return render(request, 'sub.html', {'permutations': permutations, 'input_string': input_string})
    return render(request, 'sub.html')

# Your college is holding several technical courses in Summer.(model Student)
def mode(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'i.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputform()
    return render(request,'i.html',{'form':form1})

# Take any number from 1 to 10 as an input from a HTML page.
def factorial(n):
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i   
    return   fact1


def hol(request):
    if request.method == "POST":
        form1 = inputform1(request.POST)
        if form1.is_valid():
            number = form1.cleaned_data['n']
            result = factorial(number)
            return render(request, 'i1.html', {'form': form1, 'result': result})
    else:
        form1 = inputform1()
    return render(request, 'i1.html', {'form': form1})
# icic accounts
def icic(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
          Customer = form1.save()
          return render(request, 'i.html', {'form': form1, 'param1': f"Account No: {Customer.account_no}"})
    else:
        form1=inputform()
    return render(request,'i.html',{'form':form1})

