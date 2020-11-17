from django.contrib.auth import login
from django.db.models import query, Count, Min
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.postgres.search import SearchVector

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from users.models import User

# Create your views here.

def questions_list(request):
    questions = Question.objects.all()
    return render(request, "questions/questions_list.html", {
        "questions": questions
    })

def search_qs(request):
    query = request.GET.get("qs")
    if query is not None:
        questions = Question.objects.annotate(
            search=SearchVector("title", 'body')
        ).filter(search=query)
    else:
        questions = None
    return render(request, 'questions/search_qs.html', {
        'questions': questions,
        'query': query or ""
    })

@login_required
def add_question(request):
    if request.method == "GET":
        form = QuestionForm()
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect(to='questions_list')
    return render(request, 'questions/add_question.html', {'form': form})

@login_required
def delete_question(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == "POST":
        question.delete()
        return redirect("questions_list")
    return render(request, "questions/delete_question.html", {'questions': questions} )

def question_detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    answers = question.answers.all()
    form = AnswerForm()
    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect(to="question_detail", pk=question_pk)
    return render(request, "questions/question_detail.html", {
        'question': question,
        'answers': answers,
        'question_pk': question_pk,
    })

# Answers views

@login_required
def add_answer(request, question_pk):
    if request.method == 'GET':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        question = get_object_or_404(Question, pk=question_pk)
        if form.is_valid():
            print(form)
            answer = form.save(commit=False)
            answer.author = request.user
            answer.answered_for = question
            answer.save()
            return redirect(to='question_detail', question_pk=question_pk)
    return render(request, 'questions/add_answer.html', 
    {'form':form, 'question_pk': question_pk})


@login_required
def delete_answer(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if request.method == "POST":
        question = answer.answered_for.get()
        question_pk = question.pk
        answer.delete()
        return redirect('question_detail', question_pk=question_pk)
    return render(request, "questions/delete_answer.html", {'answer':answer})

def answers_list(request):
    answers = request.question.answers.all()
    return render(request, 'questions/answers_list.html', {'answers': answers})

def answer_detail(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    return render(request, 'questions/answer_detail.html', {'answer':answer})