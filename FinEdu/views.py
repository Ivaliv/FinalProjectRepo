import random

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from FinEdu.models import Question, Answer


def index(request):
    return render(request, 'index.html', context=None)


def quizzes(request):
    questions = Question.objects.all()
    random.shuffle(list(questions))
    answers = Answer.objects.all()
    random.shuffle(list(answers))
    if len(questions) > 10:
        # todo
        questions = questions[:10]
    context = {'questions': questions, 'answers': answers}
    return render(request, 'quizzes.html', context=context)


class LoginView:
    pass


class LogoutView:
    pass
