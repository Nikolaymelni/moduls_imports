import datetime
from application.db.people import get_empoyees
from application.salary import calculate_salary

if __name__ == '__main__':

    get_empoyees()
    calculate_salary()

    dt_now = datetime.datetime.now()

    print(dt_now)
