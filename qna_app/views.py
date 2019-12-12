from django.shortcuts import render,redirect
from .models import QuestionModel,CategoryModel 
from .forms import QuestionForm # import form from forms.py
from django.http import HttpResponse

from django.views.generic import CreateView

class QuestionModelCreateView(CreateView):
    model = QuestionModel
    fields = '__all__'

def vote_question(request,id):
    instance = QuestionModel.objects.get(id=id)
    vote = instance.question_votes + 1
    instance.question_votes = vote
    instance.save()
    return redirect('qna:read')



def addquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            try: 
                form.save()
                return HttpResponse('Submitted')
            except:
                return HttpResponse('Failed')
        
        else:
            print(form.errors)
            return HttpResponse(form.errors)
        
    else:    
        # form = QuestionForm
        category = CategoryModel.objects.all()
        return render(request,'questionmodel_create.html',{'category':category})


def question(requests):
    question = QuestionModel.objects.all()
    return render(requests,'questionmodel_list.html',{'question':question})

def update_question(request ,id):
    question = QuestionModel.objects.get(id=id)
    if request.method == "POST":
            form = QuestionForm(request.POST, request.FILES, instance=question)
            print(form)
            if form.is_valid():
                try:                    
                    form.save()
                    return redirect('qna:read')

                except:
                    return HttpResponse('failure')

            else:
                return HttpResponse(form.errors)

    else:
        form = QuestionForm(instance=question)
        return render(request,'questionmodel_update.html',{'form':form})

def delete_question(requests,id):
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')