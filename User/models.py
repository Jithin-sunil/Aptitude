from django.db import models
from Guest.models import *
from Master.models import *


# Create your models here.
class tbl_complaints(models.Model):
    complaint_title=models.CharField(max_length=40)
    conplaint_content=models.CharField(max_length=100)
    complaint_reply=models.CharField(max_length=100,null=True)
    complaint_stautus=models.IntegerField(default=0)
    complaint_date=models.DateField(auto_now_add=True)
    master=models.ForeignKey(tbl_master,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)

class tbl_feedback(models.Model):
    feedback_title=models.CharField(max_length=40)
    feedback_content=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    master=models.ForeignKey(tbl_master,on_delete=models.CASCADE,null=True)

class tbl_questionhead(models.Model):
    questionhead_date=models.DateField(auto_now_add=True)
    questionhead_status=models.IntegerField(default=0)
    questionhead_code=models.CharField(max_length=40,null=True)
    questionhead_level=models.ForeignKey(tbl_level,on_delete=models.CASCADE)
    questionhead_subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_questionbody(models.Model):
    questionhead_id=models.ForeignKey(tbl_questionhead,on_delete=models.CASCADE,null=True)
    question_id=models.ForeignKey(tbl_question,on_delete=models.CASCADE)

class tbl_useranswer(models.Model):
    questionanswer_id=models.ForeignKey(tbl_questionanswer,on_delete=models.CASCADE,null=True)
    questionbody_id=models.ForeignKey(tbl_questionbody,on_delete=models.CASCADE)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    useranswer_starttime=models.IntegerField(default=0)
    useranswer_endtime=models.IntegerField(default=0)
    useranswer_mark=models.IntegerField(default=0) 

