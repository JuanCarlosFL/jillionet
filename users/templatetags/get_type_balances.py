from django import template

from users.models import UserBalance

register = template.Library()


@register.simple_tag
def get_bal(bal_type, user):

    user_balance = UserBalance.objects.filter(user=user, balance_for=bal_type)
    return user_balance
