from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Master.models import *
from random import sample
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

# Create your views here.

def HomePage(request):
    return render(request,"User/HomePage.html")

def MyProfile(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/MyProfile.html",{'user':user})

def ChangePassword(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        dbpass=user.user_pass
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        cpass=request.POST.get('txt_conpass')
        if dbpass==oldpass:
            if newpass==cpass:
                user.user_pass=newpass
                user.save()
                return redirect('User:MyProfile')
            else:
                return render(request,'User/ChangePassword.html',{'msg1':"Password Does Not Match"})
        else:
            return render(request,'User/ChangePassword.html',{'msg1':"Incorrect Current Password"})
    else:
        return render(request,"User/ChangePassword.html")

def Editprofile(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        user.user_name=request.POST.get('txt_name')
        user.user_email=request.POST.get('txt_email')
        user.user_contact=request.POST.get('txt_contact')
        user.user_address=request.POST.get('txt_address')
        user.save()
        return render(request,"User/MyProfile.html",{'user':user})
    else:
        return render(request,'User/Editprofile.html',{'user':user})
    
def Complaints(request):
    com=tbl_complaints.objects.filter(user=request.session['uid'])
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        tbl_complaints.objects.create(
            complaint_title=request.POST.get("txt_subject"),
            conplaint_content=request.POST.get("txt_content"),
            user=user
        )
        return redirect('User:Complaints')
    else:
        return render(request,'User/Complaints.html',{'com':com})
    
def FeedBack(request):
    fed=tbl_feedback.objects.filter(user=request.session['uid'])
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        tbl_feedback.objects.create(
            feedback_title=request.POST.get("txt_subject"),
            feedback_content=request.POST.get("txt_content"),
            user=user
        )
        return redirect('User:FeedBack')
    else:
        return render(request,'User/FeedBack.html',{'fed':fed})
    

def ViewQuestionPaper(request):
    levels = tbl_level.objects.all()
    subjects = tbl_subject.objects.all()
    questions_data = []
    result = None
    time_limit = None

    if request.method == "POST":
        if 'btn_submit' in request.POST:  # Initial form submission
            level_id = request.POST.get('sel_level')
            subject_id = request.POST.get('sel_subject')
            
            # Store selections in session
            request.session['level_id'] = level_id
            request.session['subject_id'] = subject_id
            request.session['start_time'] = timezone.now().isoformat()
            
            # Get level time limit
            level = tbl_level.objects.get(id=level_id)
            time_limit = level.time_limit
            
            # Get questions
            questions = tbl_question.objects.filter(
                master_id__isnull=True,
                level_id=level_id,
                subject_id=subject_id
            )
            
            for question in questions:
                all_answers = tbl_questionanswer.objects.filter(question_id=question)
                correct_answer = all_answers.filter(questionanswer_correct='true').first()
                incorrect_answers = all_answers.filter(questionanswer_correct='false')
                
                if correct_answer:
                    random_incorrect = sample(
                        list(incorrect_answers),
                        min(3, incorrect_answers.count())
                    )
                    options = [correct_answer] + random_incorrect
                    shuffled_options = sample(options, len(options))
                    
                    questions_data.append({
                        'question': question,
                        'options': shuffled_options,
                        'correct_answer': correct_answer
                    })

        elif 'btn_submit_answers' in request.POST or 'time_up' in request.POST:  # Answer submission or time up
            level_id = request.session.get('level_id')
            subject_id = request.session.get('subject_id')
            
            questions = tbl_question.objects.filter(
                master_id__isnull=True,
                level_id=level_id,
                subject_id=subject_id
            )
            
            correct_count = 0
            total_questions = questions.count()
            
            for question in questions:
                selected_answer_id = request.POST.get(f'question_{question.id}')
                correct_answer = tbl_questionanswer.objects.filter(
                    question_id=question,
                    questionanswer_correct='true'
                ).first()
                
                if selected_answer_id and correct_answer:
                    if int(selected_answer_id) == correct_answer.id:
                        correct_count += 1
            
            result = {
                'correct': correct_count,
                'total': total_questions,
                'percentage': (correct_count / total_questions * 100) if total_questions > 0 else 0
            }
            
            # Clear session
            request.session.pop('level_id', None)
            request.session.pop('subject_id', None)
            request.session.pop('start_time', None)

    # If questions are loaded but no result yet, get time limit
    if questions_data and not result:
        level_id = request.session.get('level_id')
        if level_id:
            time_limit = tbl_level.objects.get(id=level_id).time_limit

    context = {
        'level': levels,
        'subject': subjects,
        'questions_data': questions_data,
        'result': result,
        'time_limit': time_limit
    }
    return render(request, 'User/ViewQuestionPaper.html', context)



def MasterQuestionPaper(request):
    levels = tbl_level.objects.all()
    subjects = tbl_subject.objects.all()
    questions_data = []
    result = None
    time_limit = None

    if request.method == "POST":
        if 'btn_submit' in request.POST:  # Initial form submission
            level_id = request.POST.get('sel_level')
            subject_id = request.POST.get('sel_subject')
            
            # Store selections in session
            request.session['level_id'] = level_id
            request.session['subject_id'] = subject_id
            request.session['start_time'] = timezone.now().isoformat()
            
            # Get level time limit
            level = tbl_level.objects.get(id=level_id)
            time_limit = level.time_limit
            
            # Get questions with master_id not null
            questions = tbl_question.objects.filter(
                master_id__isnull=False,  # Select only questions with a master_id
                level_id=level_id,
                subject_id=subject_id
            )
            
            for question in questions:
                all_answers = tbl_questionanswer.objects.filter(question_id=question)
                correct_answer = all_answers.filter(questionanswer_correct='true').first()
                incorrect_answers = all_answers.filter(questionanswer_correct='false')
                
                if correct_answer:
                    random_incorrect = sample(
                        list(incorrect_answers),
                        min(3, incorrect_answers.count())
                    )
                    options = [correct_answer] + random_incorrect
                    shuffled_options = sample(options, len(options))
                    
                    questions_data.append({
                        'question': question,
                        'options': shuffled_options,
                        'correct_answer': correct_answer
                    })

        elif 'btn_submit_answers' in request.POST or 'time_up' in request.POST:  # Answer submission or time up
            level_id = request.session.get('level_id')
            subject_id = request.session.get('subject_id')
            
            questions = tbl_question.objects.filter(
                master_id__isnull=False,  # Select only questions with a master_id
                level_id=level_id,
                subject_id=subject_id
            )
            
            correct_count = 0
            total_questions = questions.count()
            
            for question in questions:
                selected_answer_id = request.POST.get(f'question_{question.id}')
                correct_answer = tbl_questionanswer.objects.filter(
                    question_id=question,
                    questionanswer_correct='true'
                ).first()
                
                if selected_answer_id and correct_answer:
                    if int(selected_answer_id) == correct_answer.id:
                        correct_count += 1
            
            result = {
                'correct': correct_count,
                'total': total_questions,
                'percentage': (correct_count / total_questions * 100) if total_questions > 0 else 0
            }
            
            # Clear session
            request.session.pop('level_id', None)
            request.session.pop('subject_id', None)
            request.session.pop('start_time', None)

    # If questions are loaded but no result yet, get time limit
    if questions_data and not result:
        level_id = request.session.get('level_id')
        if level_id:
            time_limit = tbl_level.objects.get(id=level_id).time_limit

    context = {
        'level': levels,
        'subject': subjects,
        'questions_data': questions_data,
        'result': result,
        'time_limit': time_limit
    }
    return render(request, 'User/ViewQuestionPaper.html', context)



def Questions(request):
    qst=tbl_question.objects.all()
    subject=tbl_subject.objects.all()
    level=tbl_level.objects.all()
    if request.method == "POST" :
        sub=tbl_subject.objects.get(id=request.POST.get("sel_subject"))
        lev=tbl_level.objects.get(id=request.POST.get("sel_level"))
        code = request.POST.get("txt_code")
        tbl_questionhead.objects.create(questionhead_code=code,questionhead_subject=sub,questionhead_level=lev,user_id=tbl_user.objects.get(id=request.session['uid'])) 
        return render(request,'User/Questions.html',{'question':qst,'Subject':subject,'Level':level})
    else:
        return render(request,'User/Questions.html',{'question':qst,'Subject':subject,'Level':level})
    
def delquestion(request,did):
    tbl_question.objects.get(id=did).delete()
    return redirect('User:Questions')

def editquestion(request,eid):
    qst=tbl_question.objects.get(id=eid)
    subject=tbl_subject.objects.all()
    level=tbl_level.objects.all()
    if request.method=="POST":
        qst.question_title=request.POST.get("txt_qtitle")
        qst.subject_id=tbl_subject.objects.get(id=request.POST.get("sel_subject"))
        qst.level_id=tbl_level.objects.get(id=request.POST.get("sel_level"))    
        qst.save()
        return redirect('User:Questions')     
    else:
        return render(request,'User/Questions.html',{'edit':qst,'Subject':subject,'Level':level})
    

def Answer(request,aid):
    ans=tbl_questionanswer.objects.filter(question_id=aid)
    qst=tbl_question.objects.all()
    if request.method=="POST":
        ans=request.POST.get("txt_answer")
        qst=tbl_question.objects.get(id=aid)
        corr=request.POST.get("correct")
        tbl_questionanswer.objects.create(question_id=qst,questionanswer_option=ans,questionanswer_correct=corr)
        return redirect('User:Answer',aid)
    else:
        return render(request,'User/Answer.html',{'answer':ans,'question':qst})

def delanswer(request,qid,did):
    tbl_questionanswer.objects.get(id=did).delete()
    return redirect('User:Answer',qid)

def editanswer(request,qid,eid):
    ans=tbl_questionanswer.objects.get(id=eid)
    if request.method=="POST":
        ans.questionanswer_option=request.POST.get("txt_answer")
        ans.questionanswer_correct=request.POST.get("correct")
        ans.save()
        return redirect('User:Answer',qid)
    else:
        return render(request,'User/Answer.html',{'edit':ans})