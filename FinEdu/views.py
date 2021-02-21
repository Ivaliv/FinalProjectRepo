import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from FinEdu.models import Question, Answer


def index(request):
    return render(request, 'index.html', context=None)


@login_required
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


def results(request):
    # get all correct answers in list form
    corr_answers = list(Answer.objects.filter(correct=True).values_list('answer_text', flat=True).distinct())

    # get all the answers sent through the form
    res_query_dict = request.POST
    res_dict = res_query_dict.dict()
    res_values = res_dict.values()

    # counters
    counter_max = len(res_values) - 1
    counter_min = 0
    for r in res_values:
        if r in corr_answers:
            counter_min += 1

    context = {'counter_max': counter_max, 'counter_min': counter_min}
    return render(request, 'results.html', context)


class LoginView:
    pass


class LogoutView:
    pass
