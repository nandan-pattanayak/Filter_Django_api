from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.StudentDetails.as_view()),
    path('add/',views.ShowDetails.as_view()),
    path('ui/',views.AddMoreDetails.as_view()),
    path('student/<int:id>/destroy',views.StudentDetailsRetrieveUpdateDestroy.as_view()),
    path('stats/',views.StaticView.as_view())
]