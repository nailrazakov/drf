from college.models import Course, Lesson
from users.models import User
from django.db import models


class Payments(models.Model):
    CASH = 'cash'
    NON_CASH = 'non_cash'
    PAY_METHOD_CHOOSES = (
        (CASH, 'наличные'),
        (NON_CASH, 'перевод на счет')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    date = models.DateTimeField(auto_now=True, verbose_name="Дата платежа")
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )
    amount = models.IntegerField(verbose_name="Сумма оплаты")
    method = models.TextField(
        max_length=15, choices=PAY_METHOD_CHOOSES, default="не выбрано"
    )

    def __str__(self):
        return f"Платеж {self.amount} руб. {self.method}\n{self.user} {self.course} {self.lesson}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
