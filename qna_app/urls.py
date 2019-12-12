from django.contrib import admin
from django.urls import path
from  qna_app import views
from .views import QuestionModelCreateView
app_name = 'qna'

urlpatterns = [
    path('add/',views.addquestion,name='add'),
    path('read/',views.question,name='read'),
    # path('ans/',views.answer,name='ans'),
    path('vote_qn/<int:id>/',views.vote_question,name='vote_qn'),
    path('update/<int:id>/',views.update_question,name='update'),
    path('delete/<int:id>/',views.delete_question,name='delete'),
    path('',QuestionModelCreateView.as_view(),name='qn')
]
