from datetime import date, datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = date.today()
    current_weekday = today.weekday()  # 0 - понеділок, 6 - неділя
    
    # Початок і кінець поточного тижня
    start_of_week = today - timedelta(days=current_weekday)
    end_of_week = start_of_week + timedelta(days=6)
    
    # Початок і кінець наступного тижня
    start_of_next_week = start_of_week + timedelta(days=7)
    end_of_next_week = start_of_next_week + timedelta(days=6)
    
    # Словник для результату
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        
        # День народження цього року
        this_year_birthday = birthday.replace(year=today.year)
        
        # Якщо день народження вже пройшов, переносимо його на наступний рік
        if this_year_birthday < today:
            this_year_birthday = birthday.replace(year=today.year + 1)
        
        # Перевіряємо, чи потрапляє день народження у цей тиждень (вихідні) або наступний
        if start_of_week <= this_year_birthday <= end_of_week:  # Цей тиждень
            weekday = this_year_birthday.weekday()
            weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            if weekday in (5, 6):  # Субота або неділя
                birthdays["Monday"].append(name)  # Додаємо до понеділка
            else:
                birthdays[weekdays[weekday]].append(name)  # Додаємо до відповідного дня
        elif start_of_next_week <= this_year_birthday <= end_of_next_week:  # Наступний тиждень
            weekday = this_year_birthday.weekday()
            weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            if weekday < 5:  # Тільки будні
                birthdays[weekdays[weekday]].append(name)

    # Перетворюємо defaultdict у звичайний словник
    return dict(birthdays)

users = [
    {"name": "Alice", "birthday": datetime(1990, 12, 25).date()},  
    {"name": "Bob", "birthday": datetime(1995, 12, 30).date()},    
    {"name": "Charlie", "birthday": datetime(2000, 12, 31).date()}, 
    {"name": "Diana", "birthday": datetime(1988, 12, 29).date()}, 
]

print(get_birthdays_per_week(users))