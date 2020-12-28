import datetime

def date_by_subtracting_minutes(from_date, subtract_minutes):
    minutes_to_subtract = subtract_minutes
    current_date = from_date
    while minutes_to_subtract > 0:
        current_date -= datetime.timedelta(minutes=1)
        minutes_to_subtract -= 1
    return current_date

# #demo:
# print '10 business days from today:'
# print date_by_adding_business_days(datetime.date.today(), 5)