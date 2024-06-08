from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Insert(request):
    if request.method == "POST":
        name = request.POST.get('empname')
        salary = request.POST.get('empsal')
        Role = request.POST.get('emprole')
        Phone = request.POST.get('empphone')
        
        Employee.objects.create(EmployeeName = name,
                                EmployeeSalary = salary,
                                EmployeeRole = Role,
                                EmployeePhone = Phone,
                                )
        msg = "Insert Sucessfully"
        return render(request,'Insert.html',{'key':msg})
    return render(request,'Insert.html')
        
def Show(request):
    alldata = Employee.objects.all()
    return render(request,'Insert.html',{'alldata':alldata})

def Editpage(request,pk):
    id = Employee.objects.get(id=pk)
    alldata =  Employee.objects.all()
    return render(request,'Edit.html',{'data1':id,'alldata':alldata})

def Update(request,pk):
    Update = Employee.objects.get(id=pk)
    
    Update.EmployeeName= request.POST['empnm'] 
    Update.EmployeeSalary= request.POST['empsl'] 
    Update.EmployeeRole= request.POST['emprol'] 
    Update.EmployeePhone= request.POST['empphne'] 
    Update.save()

    all = Employee.objects.all()
    return render(request,'Insert.html',{'all':all})


def Delete(request,pk):
    del1 = Employee.objects.get(id = pk)
    del1.delete()
    # all = Employee.objects.all()
    return redirect('Show')