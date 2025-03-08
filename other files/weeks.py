from datetime import datetime, timedelta
def input_num(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print("invalid input! enter a number only!!!")

def print_week_dates(weeknumber, year = 2025):
    start_of_year = datetime(2024, 12, 30)
    day_to_add = (weeknumber - 1) * 7
    week_start_date = start_of_year + timedelta(days = day_to_add)

    for i in range(7):
        day_date = week_start_date +  timedelta(days = i)
        print(day_date.strftime("%A, %B %d, %Y"))

def get_week_number():
    while True:
        week_number = input_num("Enter the week number (1-52), or enter [-1] to exit the program: ")
        if week_number == -1:
            print("exiting the program....")
            break

        if (week_number >= 1 and week_number <= 52):

            print(f"the week number {week_number} has the week")
            print_week_dates(week_number)
        else:
            print("Invalid week number! Please enter a number between 1 and 52 only")

get_week_number()

 