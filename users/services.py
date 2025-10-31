from college.models import Course, Lesson
from users.models import User
from django.db import models
import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


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
    link = models.CharField(verbose_name='ссылка на платеж', blank=True, null=True)

    session_id = models.CharField(verbose_name='id-платежа', blank=True, null=True)

    def __str__(self):
        return f"Платеж {self.amount} руб. {self.method}\n{self.user} {self.course} {self.lesson}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"


def create_stripe_product(name):
    """ Создаем stripe продукт. """
    product = stripe.Product.create(name=name)
    return product


def create_stripe_price(amount, product_id):
    """Создает цену в Stripe"""
    price = stripe.Price.create(
        currency='usd',
        unit_amount=int(amount) * 100,
        product=product_id,
    )
    return price


def create_stripe_session(price):
    """Создает сессию оплаты в Stripe"""
    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': price.get('id'),
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return session.get('id'), session.get('url')
