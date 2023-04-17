from app.db.employees import search_employees
from app.salary import calculate_salary
from datetime import datetime


if __name__ == '__main__':
    print(datetime.now())
    search_employees()
    calculate_salary()