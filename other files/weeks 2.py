from datetime import datetime, timedelta

def input_num(num): # function for taking a input
      while True:
        try:
            return float(input(num))
        except ValueError:
            print("invalid please enter a number only!!!")
def print_week_dates(week_number, year=2025):
    # Set December 30, 2024, as the start date for week 1 as instructed
    start_of_week_1 = datetime(2024, 12, 30)
    
    days_to_add = (week_number - 1) * 7
    week_start_date = start_of_week_1 + timedelta(days=days_to_add)
    
    # Print the dates from Monday to Sunday for that week
    for i in range(7):
        day_date = week_start_date + timedelta(days=i)
        print(day_date.strftime("%A, %B %d, %Y"))

def get_week_number():
    while True:
            # Ask the user for week number
            week_number = input_num("Enter the week number (1-52), or enter [-1] to exit the program: ")
            
            if week_number == -1:
                print("Exiting program...")
                break  # Exit the loop if the user enters -1

            # Check if the week number is valid
            if 1 <= week_number <= 52:
                print(f"Dates for week {week_number} starting from December 30, 2024:")
                print_week_dates(week_number)
            else:
                print("Please enter a valid week number between 1 and 52.")

# Run the function to keep asking for a week number
get_week_number()
