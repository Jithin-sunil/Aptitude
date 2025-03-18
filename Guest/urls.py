from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('UserRegistration/',views.UserRegistration,name='UserRegistration'),
    path('AjaxPlace/',views.AjaxPlace,name='AjaxPlace'),
    path('Login/',views.Login,name='Login'),
    path('MasterRegistration/',views.MasterRegistration,name='MasterRegistration'),
    path('',views.index,name='index'),

]