from datetime import datetime, timedelta

def get_date_five_days_ago():
    current_date = datetime.now()
    date_five_days_ago = current_date - timedelta(days=5)
    return date_five_days_ago

def print_yesterday_today_tomorrow():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday, today, tomorrow

def current_time_without_microseconds():
    current_time = datetime.now()
    time_without_microseconds = current_time.replace(microsecond=0)
    return time_without_microseconds

def calculate_difference_in_seconds(date1, date2):
    difference = (date2 - date1).total_seconds()
    return difference

# Task 1: Subtract five days from the current date
five_days_ago = get_date_five_days_ago()
print(f"Five days ago, the date was: {five_days_ago.strftime('%Y-%m-%d')}")

# Task 2: Print yesterday, today, tomorrow
yesterday, today, tomorrow = print_yesterday_today_tomorrow()
print(f"Yesterday was: {yesterday.strftime('%Y-%m-%d')}")
print(f"Today is: {today.strftime('%Y-%m-%d')}")
print(f"Tomorrow will be: {tomorrow.strftime('%Y-%m-%d')}")

# Task 3: Drop microseconds from datetime
time_no_microseconds = current_time_without_microseconds()
print(f"Current time without microseconds: {time_no_microseconds}")

# Task 4: Calculate two date difference in seconds
# Example dates
date1 = datetime(2024, 2, 11, 12, 0, 0)
date2 = datetime(2024, 2, 16, 12, 0, 0)
difference_seconds = calculate_difference_in_seconds(date1, date2)
print(f"The difference between dates in seconds is: {difference_seconds}")
