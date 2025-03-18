from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Master.models import *
from User.models import *

# Create your views here.
def District(request):
    dis=tbl_district.objects.all()
    if(request.method=="POST"):
        District=request.POST.get("txt_district")
        tbl_district.objects.create(district_name=District)
        return render(request,'Admin/District.html',{'district':dis})
    else:
        return render(request,'Admin/District.html',{'district':dis})

def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')

def editdistrict(request,eid):
    dis=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        dis.district_name=request.POST.get("txt_district")
        dis.save()
        return redirect('Admin:District')     
    else:
        return render(request,'Admin/District.html',{'edit':dis})

    

def Category(request):
    cat=tbl_category.objects.all()
    if(request.method=="POST"):
        Category=request.POST.get("txt_category")
        tbl_category.objects.create(category_name=Category)
        return render(request,'Admin/Category.html',{'category':cat})
    else:
        return render(request,'Admin/Category.html',{'category':cat})

def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect('Admin:Category')

def editcategory(request,eid):
    cat=tbl_category.objects.get(id=eid)
    if request.method=='POST':
        cat.category_name=request.POST.get("txt_category")
        cat.save()
        return redirect('Admin:Category')
    else:
        return render(request,'Admin/Category.html',{'edit':cat})


def AdminRegistration(request):
    adm=tbl_adminreg.objects.all()
    if(request.method=="POST"):
        Name=request.POST.get("txt_name")
        Email=request.POST.get("txt_email")
        Password=request.POST.get("txt_password")
        tbl_adminreg.objects.create(admin_name=Name,admin_email=Email,admin_pass=Password)
        return render(request,'Admin/AdminRegistration.html',{'admin':adm})
    else:
        return render(request,'Admin/AdminRegistration.html',{'admin':adm})
    
def deladmin(request,did):
    adm=tbl_adminreg.objects.get(id=did).delete()
    return redirect('Admin:AdminRegistration')

def editadmin(request,eid):
    adm=tbl_adminreg.objects.get(id=eid)
    if request.method=='POST':
        adm.admin_name=request.POST.get("txt_name")
        adm.admin_email=request.POST.get("txt_email")
        adm.admin_pass=request.POST.get("txt_password")
        adm.save()
        return redirect('Admin:AdminRegistration')
    else:
        return render(request,'Admin/AdminRegistration.html',{'edit':adm})
    

def Place(request):
    DistrictData=tbl_district.objects.all()
    PlaceData=tbl_place.objects.all()
    if request.method=="POST":
        place=request.POST.get('txt_place')
        dis=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=place,district=dis)
        return render(request,'Admin/Place.html',{'District':DistrictData,'Place':PlaceData})
    else:
        return render(request,'Admin/Place.html',{'District':DistrictData,'Place':PlaceData})
    
def delpalce(request,did):
    place=tbl_place.objects.get(id=did).delete()
    return redirect('Admin:Place')

def editplace(request,eid):
    DistrictData=tbl_district.objects.all()
    place=tbl_place.objects.get(id=eid)
    if request.method=='POST':
        place.district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        place.place_name=request.POST.get("txt_place")
        place.save()
        return redirect('Admin:Place')
    else:
        return render(request,'Admin/Place.html',{'edit':place,'District':DistrictData})


def SubCategory(request):
    CategoryData=tbl_category.objects.all()
    SubCategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get('txt_subcategory')
        cat=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcategory_name=subcategory,category=cat)
        return render(request,'Admin/SubCategory.html',{'Category':CategoryData,'SubCategory':SubCategory})
    else:
        return render(request,'Admin/SubCategory.html',{'Category':CategoryData,'SubCategory':SubCategory})
    
def delsubcat(request,did):
    subcategory=tbl_subcategory.objects.get(id=did).delete()
    return redirect('Admin:SubCategory.html')

def editsubcat(request,eid):
    CategoryData=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.get(id=eid)
    if request.method=='POST':
        subcategory.category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategory.subcategory_name=request.POST.get("txt_subcategory")
        subcategory.save()
        return redirect('Admin:Place')
    else:
        return render(request,'Admin/Place.html',{'edit':subcategory,'Category':CategoryData})


def MasterApproval(request):
    master=tbl_master.objects.all()
    return render(request,"Admin/MasterApproval.html",{'master':master})

def accept(request,acid):
    acc=tbl_master.objects.get(id=acid)
    acc.master_vstatus=1
    acc.save()
    return redirect('Admin:MasterApproval')

def reject(request,reid):
    acc=tbl_master.objects.get(id=reid)
    acc.master_vstatus=2
    acc.save()
    return redirect('Admin:MasterApproval')


def HomePage(request):
    return render(request,'Admin/HomePage.html')


def Subjects(request):
    sub=tbl_subject.objects.all()
    if request.method == "POST" :
        SubName=request.POST.get("txt_subname")
        tbl_subject.objects.create(subject_name=SubName)
        return(render(request,'Admin/Subjects.html',{'subject':sub}))
    else:
        return(render(request,'Admin/Subjects.html',{'subject':sub}))
    
def delsubject(request,did):
    tbl_subject.objects.get(id=did).delete()
    return redirect('Admin:Subjects')

def editsubject(request,eid):
    dis=tbl_subject.objects.get(id=eid)
    if request.method=="POST":
        dis.subject_name=request.POST.get("txt_subname")
        dis.save()
        return redirect('Admin:Subjects')     
    else:
        return render(request,'Admin/Subjects.html',{'edit':dis})
    
def Levels(request):
    lev=tbl_level.objects.all()
    if request.method == "POST" :
        levname=request.POST.get("txt_level")
        tbl_level.objects.create(level_name=levname)
        return(render(request,'Admin/Levels.html',{'level':lev}))
    else:
        return(render(request,'Admin/Levels.html',{'level':lev}))
    
def dellevel(request,did):
    tbl_level.objects.get(id=did).delete()
    return redirect('Admin:Levels')

def editlevel(request,eid):
    lev=tbl_level.objects.get(id=eid)
    if request.method=="POST":
        lev.level_name=request.POST.get("txt_level")
        lev.save()
        return redirect('Admin:Levels')     
    else:
        return render(request,'Admin/Levels.html',{'edit':lev})
    


def Questions(request):
    qst=tbl_question.objects.all()
    subject=tbl_subject.objects.all()
    level=tbl_level.objects.all()
    if request.method == "POST" :
        qn=request.POST.get("txt_qtitle")
        sub=tbl_subject.objects.get(id=request.POST.get("sel_subject"))
        lev=tbl_level.objects.get(id=request.POST.get("sel_level"))
        tbl_question.objects.create(question_title=qn,subject_id=sub,level_id=lev)
        return render(request,'Admin/Questions.html',{'question':qst,'Subject':subject,'Level':level})
    else:
        return render(request,'Admin/Questions.html',{'question':qst,'Subject':subject,'Level':level})
    
def delquestion(request,did):
    tbl_question.objects.get(id=did).delete()
    return redirect('Admin:Questions')

def editquestion(request,eid):
    qst=tbl_question.objects.get(id=eid)
    subject=tbl_subject.objects.all()
    level=tbl_level.objects.all()
    if request.method=="POST":
        qst.question_title=request.POST.get("txt_qtitle")
        qst.subject_id=tbl_subject.objects.get(id=request.POST.get("sel_subject"))
        qst.level_id=tbl_level.objects.get(id=request.POST.get("sel_level"))    
        qst.save()
        return redirect('Admin:Questions')     
    else:
        return render(request,'Admin/Questions.html',{'edit':qst,'Subject':subject,'Level':level})
    

def Answer(request,aid):
    ans=tbl_questionanswer.objects.filter(question_id=aid)
    qst=tbl_question.objects.all()
    if request.method=="POST":
        ans=request.POST.get("txt_answer")
        qst=tbl_question.objects.get(id=aid)
        corr=request.POST.get("correct")
        tbl_questionanswer.objects.create(question_id=qst,questionanswer_option=ans,questionanswer_correct=corr)
        return redirect('Admin:Answer',aid)
    else:
        return render(request,'Admin/Answer.html',{'answer':ans,'question':qst})

def delanswer(request,qid,did):
    tbl_questionanswer.objects.get(id=did).delete()
    return redirect('Admin:Answer',qid)

def editanswer(request,qid,eid):
    ans=tbl_questionanswer.objects.get(id=eid)
    if request.method=="POST":
        ans.questionanswer_option=request.POST.get("txt_answer")
        ans.questionanswer_correct=request.POST.get("correct")
        ans.save()
        return redirect('Admin:Answer',qid)
    else:
        return render(request,'Admin/Answer.html',{'edit':ans})
    
def ViewComplaints(request):
    user=tbl_user.objects.all()
    usr=tbl_complaints.objects.filter(user__in=user)

    master=tbl_master.objects.all()
    mast=tbl_complaints.objects.filter(master__in=master)
    return render(request,'Admin/ViewComplaints.html',{'usr':usr,'mast':mast})

def Reply(request,id):
    reply=tbl_complaints.objects.get(id=id)
    if request.method=="POST":
        reply.complaint_reply=request.POST.get("txt_reply")
        reply.save()
        return redirect('Admin:ViewComplaints')     
    else:
        return render(request,'Admin/Reply.html')
    
def ViewFeedBack(request):
    user=tbl_user.objects.all()
    usr=tbl_feedback.objects.filter(user__in=user)

    master=tbl_master.objects.all()
    mast=tbl_feedback.objects.filter(master__in=master)
    return render(request,'Admin/ViewFeedBack.html',{'usr':usr,'mast':mast})