from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


SECURITY_QUESTIONS = [
    ("pet", "What was the name of your first pet?"),
    ("school", "What is the name of your first school?"),
    ("city", "In which city were you born?"),
    ("nickname", "What was your childhood nickname?"),
    ("book", "What is your favourite book?"),
]


class SecurityProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="security_profile"
    )

    question = models.CharField(
        max_length=20,
        choices=SECURITY_QUESTIONS
    )

    answer_hash = models.CharField(max_length=255)

    def set_answer(self, raw_answer):
        self.answer_hash = make_password(raw_answer.strip().lower())

    def check_answer(self, raw_answer):
        return check_password(raw_answer.strip().lower(), self.answer_hash)

    def get_question_text(self):
        return dict(SECURITY_QUESTIONS).get(self.question, "")

    def __str__(self):
        return f"Security question for {self.user.username}"
