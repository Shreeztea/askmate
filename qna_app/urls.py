from django.contrib import admin
from django.urls import path
from  qna_app import views

app_name = 'qna'

urlpatterns = [
    path('add/',views.addquestion,name='add'),
    path('read/',views.question,name='read'),
    path('ans/',views.question,name='ans'),
    path('vote_qn/',views.question,name='vote_qn'),
    path('update/<int:id>',views.question,name='update'),
    path('delete/<int:id>',views.question,name='delete'),
]
