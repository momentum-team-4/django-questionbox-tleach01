from django.contrib.auth import login
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from users.models import User

# Create your views here.

def questions_list(request):
    question = Question.objects.all()
    context = {'questions': question}
    return render(request, "questions/questions_list.html", context)


@login_required
def add_question(request):
    form = QuestionForm(data=request.POST)
    if form.is_valid():
        question = form.save(commit=False)
        question.user = request.user
        question.save()
        return redirect(to="question_detail", pk=question.pk)
    form = QuestionForm()

    return render(request, "templates/ask_question.html", {'form': form})

@login_required
def delete_question(request, pk):
    question = Question.objects.get(pk=pk)
    question.delete()
    user = User.objects.get(pk=request.user.pk)
    questions = Question.objects.all()
    return render(request, "users/userprofile.html", {'user': user, 'questions': questions} )

def question_detail(request, pk):
    form = AnswerForm()
    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(questions=question)
    return render(request, "questions/question_detail.html", {'question':question, 'answers':answers, 'form':form})

@login_required
def add_answer(request, pk):
    if request.method == 'GET':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            print(form)
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            return redirect(to='question_detail', pk=pk)
    return render(request, 'questions/add_answer.html', {'form':form})