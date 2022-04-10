import datetime


def get_datetime_ctx():
    date = datetime.datetime.now()
    return {"date": {"day": date.day, "month": date.strftime("%B"), "year": date.year}}
