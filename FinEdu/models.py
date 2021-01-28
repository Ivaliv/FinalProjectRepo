from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=250)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField()

    def __str__(self):
        return f'{self.answer_text}({self.correct})'
