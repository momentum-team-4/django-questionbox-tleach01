from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from users.models import User

# Create your views here.

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