from django.shortcuts import render,redirect
from Guest.models import *

# Create your views here.
def UserRegistration(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        Name=request.POST.get("txt_name")
        Contact=request.POST.get("txt_contact")
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_pass")
        Address=request.POST.get("txt_address")
        Photo=request.FILES.get("btn_photo")
        Place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_user.objects.create(user_name=Name,user_contact=Contact,user_email=Email,user_pass=Password,user_address=Address,user_photo=Photo,place=Place)
        return render(request,'Guest/UserRegistration.html')    
    else:
        return render(request,'Guest/UserRegistration.html',{'district':dis})
    
def AjaxPlace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/AjaxPlace.html',{'place':place})

def Login(request):
    if request.method == "POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pass")

        usercount=tbl_user.objects.filter(user_email=email,user_pass=password).count()
        admincount=tbl_adminreg.objects.filter(admin_email=email,admin_pass=password).count()
        mastercount=tbl_master.objects.filter(master_email=email,master_pass=password).count()

        if usercount>0:
            user=tbl_user.objects.get(user_email=email,user_pass=password)
            request.session["uid"]=user.id
            return redirect("User:HomePage")
        elif admincount>0:
            admin=tbl_adminreg.objects.get(admin_email=email,admin_pass=password)
            request.session["aid"]=admin.id
            return redirect("Admin:HomePage")
        elif mastercount>0:
            master=tbl_master.objects.get(master_email=email,master_pass=password)
            request.session["mid"]=master.id
            return redirect("Master:HomePage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid email or password"})
    else:
        return render(request,"Guest/Login.html")

def MasterRegistration(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        Name=request.POST.get("txt_name")
        Contact=request.POST.get("txt_contact")
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_pass")
        Address=request.POST.get("txt_address")
        Photo=request.FILES.get("btn_photo")
        Proof=request.FILES.get("txt_proof")
        Place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_master.objects.create(master_name=Name,master_contact=Contact,master_email=Email,master_pass=Password,master_address=Address,master_photo=Photo,master_proof=Proof,place=Place)
        return render(request,'Guest/MasterRegistration.html')
    else:
        return render(request,'Guest/MasterRegistration.html',{'district':dis})
    
def index(request):
    return render(request,'Guest/index.html')