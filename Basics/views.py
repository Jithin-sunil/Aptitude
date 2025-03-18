from django.shortcuts import render

# Create your views here.
def Add(request):
    if request.method=="POST":
        number1=int(request.POST.get("txt_num1"))
        number2=int(request.POST.get("txt_num2"))
        result=number1+number2
        return render(request,'Basics/Add.html',{'Sum':result})
    else:
        return render(request,'Basics/Add.html')
def Largest(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number1"))
        num2=int(request.POST.get("txt_number2"))
        num3=int(request.POST.get("txt_number3"))
        if(num1>num2):
            if(num1>num3):
                Largest=num1
                if(num2<num3):
                    Smallest=num2
                else:
                    Smallest=num3
            else:
                Largest=num3
                if(num1<num2):
                    Smallest=num1
                else:
                    Smallest=num2
        else:
            if(num2>num3):
                Largest=num2
                if(num1<num3):
                    Smallest=num1
                else:
                    Smallest=num3
            else:
                Largest=num3
                if(num1<num2):
                    Smallest=num1
                else:
                    Smallest=num2
        return render(request,'Basics/Largest.html',{'Largest':Largest,'Smallest':Smallest})
    else:
        return render(request,'Basics/Largest.html')
def Calculator(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number1"))
        num2=int(request.POST.get("txt_number2"))
        btn=request.POST.get("btn")
        if(btn=="+"):
            result=num1+num2
        elif(btn=="-"):
            result=num1-num2
        elif(btn=="*"):
            result=num1*num2
        elif(btn=="/"):
            result=num1/num2
        return render(request,'Basics/Calculator.html',{'Result':result})
    else:
        return render(request,'Basics/Calculator.html')