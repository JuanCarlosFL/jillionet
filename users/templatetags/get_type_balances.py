from django import template

from users.models import UserBalance

register = template.Library()


@register.simple_tag
def get_bal(bal_type, user):

    user_balance = UserBalance.objects.filter(user=user, balance_for=bal_type)
    return user_balance


@register.simple_tag
def market_currency_balance(pair, user):
    _, currecy_code = pair.split('_')

    try:
        #user_balance =
        if user.is_authenticated:
            return user.get_currency_balance('spot', currecy_code)['amount']
        else:
            return 0
    except TypeError:
        return 0
