from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Complaints/',views.Complaints,name='Complaints'),
    path('FeedBack/',views.FeedBack,name='FeedBack'),
    path('ViewQuestionPaper/',views.ViewQuestionPaper,name='ViewQuestionPaper'),
    path('MasterQuestionPaper/',views.MasterQuestionPaper,name='MasterQuestionPaper'),


     path('Questions/',views.Questions,name='Questions'),
    path('delquestion/<int:did>',views.delquestion,name="delquestion"),
    path('editquestion/<int:eid>',views.editquestion,name="editquestion"),

    path('Answer/<int:aid>',views.Answer,name='Answer'),
    path('delanswer/<int:did>/<int:qid>',views.delanswer,name="delanswer"),
    path('editanswer/<int:eid>/<int:qid>',views.editanswer,name="editanswer"),
    
    
]