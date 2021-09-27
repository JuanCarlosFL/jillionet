from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from users.forms import UserChangeForm, UserCreationForm
from .models import UserBalance, UserLevel, BalanceFor

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "phone_number", "email", "level", "jillion_public_key")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "is_superuser"]
    search_fields = ["username"]

    add_fieldsets = auth_admin.UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_code', 'amount', 'get_balance_for', 'action', 'updated_at']

    def get_code(self, obj):
        try:
            return obj.currency.code
        except:
            return None

    get_code.short_description = 'Currency Code'
    get_code.admin_order_field = 'currency__code'

    def get_balance_for(self, obj):
        try:
            return obj.balance_for.name
        except:
            return None

    get_balance_for.short_description = 'Balance for'
    get_balance_for.admin_order_field = 'balance_for__name'


@admin.register(UserLevel)
class User_level_field(admin.ModelAdmin):
    list_display = ['level_key', 'borrow_interest', 'maker_taker', 'inicial_balance_USDT', 'free_balance_JILL',
                    'inicial_balance_USDT', 'max_withdraw_USDT', 'Jillion_hold_trigger', 'Futures_leverage']


admin.site.register(BalanceFor)