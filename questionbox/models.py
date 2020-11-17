from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField
from users.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    favorited_by = ManyToManyField(to=User, related_name="favorite_question", blank=True)

    def users_questions(self, author):
        if user.is_authenticated:
            questions = self.filter(author=author)
        else:
            questions = None
        return questions

    def __str__(self):
        return f'({self.author}) {self.title} ({self.date_added})'


class Answer(models.Model):
    body = models.TextField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    answered_for = ForeignKey(Question, on_delete=CASCADE, null=False, blank=False, related_name="answers")

    def get_answers(self, answered_for):
        answers = self.filter(answered_for=answered_for)

        if answers is None:
            return None
        else:
            return answers

    def __str__(self):
        return f"({self.author}) {self.body} ({self.date_added})"
