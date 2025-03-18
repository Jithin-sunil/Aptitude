from django.db import models
from Guest.models import *

# Create your models here.

class tbl_question(models.Model):
    question_title=models.CharField(max_length=100)
    master_id=models.ForeignKey(tbl_master,on_delete=models.CASCADE,null=True)
    subject_id=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    level_id=models.ForeignKey(tbl_level,on_delete=models.CASCADE)

class tbl_questionanswer(models.Model):
    question_id=models.ForeignKey(tbl_question,on_delete=models.CASCADE)
    questionanswer_option=models.CharField(max_length=40)
    questionanswer_correct=models.CharField(max_length=40)
        