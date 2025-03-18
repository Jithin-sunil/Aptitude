from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Master.models import *


# Create your views here.

def HomePage(request):
    return render(request,'Master/HomePage.html')

def MyProfile(request):
    master=tbl_master.objects.get(id=request.session['mid'])
    return render(request,"Master/MyProfile.html",{'master':master})

def ChangePassword(request):
    master=tbl_master.objects.get(id=request.session['mid'])
    if request.method=="POST":
        dbpass=master.master_pass
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        cpass=request.POST.get('txt_conpass')
        if dbpass==oldpass:
            if newpass==cpass:
                master.master_pass=newpass
                master.save()
                return render(request,'Master/ChangePassword.html',{'msg':"Password Updated"})
            else:
                return render(request,'Master/ChangePassword.html',{'msg1':"Password Does Not Match"})
        else:
            return render(request,'Master/ChangePassword.html',{'msg1':"Incorrect Current Password"})
    else:
        return render(request,"Master/ChangePassword.html")

def Editprofile(request):
    master=tbl_master.objects.get(id=request.session['mid'])
    if request.method=="POST":
        master.master_name=request.POST.get('txt_name')
        master.master_email=request.POST.get('txt_email')
        master.master_contact=request.POST.get('txt_contact')
        master.master_address=request.POST.get('txt_address')
        master.save()
        return render(request,"Master/MyProfile.html",{'master':master})
    else:
        return render(request,'Master/Editprofile.html',{'master':master})
    
def ViewQuestions(request):
    qst=tbl_question.objects.all()
    subject=tbl_subject.objects.all()
    level=tbl_level.objects.all()
    return render(request,'Master/ViewQuestions.html',{'question':qst,'Subject':subject,'Level':level})

def ViewAnswer(request,aid):
    ans=tbl_questionanswer.objects.filter(question_id=aid)
    qst=tbl_question.objects.all()
    return render(request,'Master/ViewAnswer.html',{'answer':ans,'question':qst})

def Complaints(request):
    com=tbl_complaints.objects.filter(master=request.session['mid'])
    master=tbl_master.objects.get(id=request.session['mid'])
    if request.method == "POST":
        tbl_complaints.objects.create(
            complaint_title=request.POST.get("txt_subject"),
            conplaint_content=request.POST.get("txt_content"),
            master=master
        )
        return redirect('Master:Complaints')
    else:
        return render(request,'Master/Complaints.html',{'com':com})
    
def FeedBack(request):
    fed=tbl_feedback.objects.filter(master=request.session['mid'])
    master=tbl_master.objects.get(id=request.session['mid'])
    if request.method == "POST":
        tbl_feedback.objects.create(
            feedback_title=request.POST.get("txt_subject"),
            feedback_content=request.POST.get("txt_content"),
            master=master
        )
        return redirect('Master:FeedBack')
    else:
        return render(request,'Master/FeedBack.html',{'fed':fed})


def Questions(request):
    qst=tbl_question.objects.all()
    subject=tbl_subject.objects.all()
    level=tbl_level.objects.all()
    if request.method == "POST" :
        qn=request.POST.get("txt_qtitle")
        sub=tbl_subject.objects.get(id=request.POST.get("sel_subject"))
        lev=tbl_level.objects.get(id=request.POST.get("sel_level"))
        tbl_question.objects.create(question_title=qn,subject_id=sub,level_id=lev,master_id=tbl_master.objects.get(id=request.session['mid'])) 
        return render(request,'Master/Questions.html',{'question':qst,'Subject':subject,'Level':level})
    else:
        return render(request,'Master/Questions.html',{'question':qst,'Subject':subject,'Level':level})
    
def delquestion(request,did):
    tbl_question.objects.get(id=did).delete()
    return redirect('Master:Questions')

def editquestion(request,eid):
    qst=tbl_question.objects.get(id=eid)
    subject=tbl_subject.objects.all()
    level=tbl_level.objects.all()
    if request.method=="POST":
        qst.question_title=request.POST.get("txt_qtitle")
        qst.subject_id=tbl_subject.objects.get(id=request.POST.get("sel_subject"))
        qst.level_id=tbl_level.objects.get(id=request.POST.get("sel_level"))    
        qst.save()
        return redirect('Master:Questions')     
    else:
        return render(request,'Master/Questions.html',{'edit':qst,'Subject':subject,'Level':level})
    

def Answer(request,aid):
    ans=tbl_questionanswer.objects.filter(question_id=aid)
    qst=tbl_question.objects.all()
    if request.method=="POST":
        ans=request.POST.get("txt_answer")
        qst=tbl_question.objects.get(id=aid)
        corr=request.POST.get("correct")
        tbl_questionanswer.objects.create(question_id=qst,questionanswer_option=ans,questionanswer_correct=corr)
        return redirect('Master:Answer',aid)
    else:
        return render(request,'Master/Answer.html',{'answer':ans,'question':qst})

def delanswer(request,qid,did):
    tbl_questionanswer.objects.get(id=did).delete()
    return redirect('Master:Answer',qid)

def editanswer(request,qid,eid):
    ans=tbl_questionanswer.objects.get(id=eid)
    if request.method=="POST":
        ans.questionanswer_option=request.POST.get("txt_answer")
        ans.questionanswer_correct=request.POST.get("correct")
        ans.save()
        return redirect('Master:Answer',qid)
    else:
        return render(request,'Master/Answer.html',{'edit':ans})