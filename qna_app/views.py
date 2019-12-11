from django.shortcuts import render,redirect
from .models import QuestionModel
from .forms import QuestionForm
from django.http import HttpResponse


# Create your views here.
def addquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')

            except:
                return HttpResponse('failure')

        else:
            return HttpResponse(form.errors)

    else:
        form = QuestionForm
        return render(request,'newquestion.html',{'form':form})


def question(requests):
    question = QuestionModel.objects.all()
    return render(requests,'questions.html',{'question':question})
