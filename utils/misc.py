import datetime
import json
from decimal import Decimal


def entries_to_remove(entries, the_dict):
    for key in entries:
        the_dict.pop(key, None)
    return the_dict


def get_number_of_months(start_month, start_yr, end_month, end_yr):
    end_date = datetime.datetime(end_yr, end_month, 1)
    start_date = datetime.datetime(start_yr, start_month, 1)
    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    return num_months


# this get the minimum non zero item
def get_min_non_zero(arr):
    new_arr = [i for i in arr if i > 0]
    if len(new_arr) == 0:
        return 1
    m = min(new_arr)
    return m


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def get_thousandth(num):
    return round(Decimal(num)/1000) * 1000
