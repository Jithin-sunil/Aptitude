from django.urls import path
from Admin import views
app_name="Admin"
urlpatterns = [
    path('District/',views.District,name='District'),
    path('deldistrict/<int:did>',views.deldistrict,name="deldistrict"),
    path('editdistrict/<int:eid>',views.editdistrict,name="editdistrict"),

    path('Category/',views.Category,name='Category'),
    path('delcategory/<int:did>',views.delcategory,name="delcategory"),
    path('editcategory/<int:eid>',views.editcategory,name="editcategory"),

    path('SubCategory/',views.SubCategory,name='SubCategory'),
    path('delsubcat/<int:did>',views.delsubcat,name="delsubcat"),
    path('editsubcat/<int:eid>',views.editsubcat,name="editsubcat"),


    path('AdminRegistration/',views.AdminRegistration,name='AdminRegistration'),
    path('deladmin/<int:did>',views.deladmin,name="deladmin"),
    path('editadmin/<int:eid>',views.editadmin,name="editadmin"),

    path('Place/',views.Place,name='Place'),
    path('delpalce/<int:did>',views.delpalce,name="delpalce"),
    path('editplace/<int:eid>',views.editplace,name="editplace"),
    
    path('MasterApproval/',views.MasterApproval,name='MasterApproval'),
    path('accept/<int:acid>',views.accept,name='accept'),
    path('reject/<int:reid>',views.reject,name='reject'),

    path('HomePage/',views.HomePage,name='HomePage'),

    path('Subjects/',views.Subjects,name='Subjects'),
    path('delsubject/<int:did>',views.delsubject,name="delsubject"),
    path('editsubject/<int:eid>',views.editsubject,name="editsubject"),

    path('Levels/',views.Levels,name='Levels'),
    path('dellevel/<int:did>',views.dellevel,name="dellevel"),
    path('editlevel/<int:eid>',views.editlevel,name="editlevel"),

    path('Questions/',views.Questions,name='Questions'),
    path('delquestion/<int:did>',views.delquestion,name="delquestion"),
    path('editquestion/<int:eid>',views.editquestion,name="editquestion"),

    path('Answer/<int:aid>',views.Answer,name='Answer'),
    path('delanswer/<int:did>/<int:qid>',views.delanswer,name="delanswer"),
    path('editanswer/<int:eid>/<int:qid>',views.editanswer,name="editanswer"),

    path('ViewComplaints/',views.ViewComplaints,name='ViewComplaints'),

    path('Reply/<int:id>',views.Reply,name='Reply'),
    
    path('ViewFeedBack/',views.ViewFeedBack,name='ViewFeedBack'),


]