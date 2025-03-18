from django.urls import path,include
from Basics import views
urlpatterns = [
    path('Add/',views.Add,name='Add'),
    path('Largest/',views.Largest,name='Largest'),
    path('Calculator/',views.Calculator,name='Calculator')
]