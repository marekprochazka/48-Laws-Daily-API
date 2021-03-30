from .models import DailyId
import random


def generate_new_daily_id():
    DailyId.objects.all().delete()
    # DailyId(random.randint(1, 48)).save() Limited to actual laws in db
    DailyId(random.randint(1, 36)).save()

