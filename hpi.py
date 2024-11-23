from datetime import datetime

def calculate_hours_and_salary(entries, hourly_rate, extra_pay_days=None, extra_rate=1.5):
    """
    Calculates the total hours worked, the total salary, and extra pay.
    
    :param entries: List of dictionaries with work entries and exits. 
                    Each dictionary should have the 'entry' and 'exit' keys in the format 'YYYY-MM-DD HH:MM'.
    :param hourly_rate: Hourly rate of pay.
    :param extra_pay_days: List of dates (in 'YYYY-MM-DD' format) on which extra pay applies.
    :param extra_rate: The multiplier for the extra pay (default is 1.5, representing 50% more).
    :return: Tuple with total hours worked, total salary including extra pay, and total extra pay.
    """
    # If no extra pay days are provided, use an empty list
    if extra_pay_days is None:
        extra_pay_days = []

    total_hours = 0.0  # Initialize total hours worked
    total_extra_pay = 0.0  # Initialize total extra pay

    # Loop through each entry in the entries list
    for entry in entries:
        # Convert 'entry' and 'exit' strings into datetime objects
        entry_time = datetime.strptime(entry['entry'], '%Y-%m-%d %H:%M')
        exit_time = datetime.strptime(entry['exit'], '%Y-%m-%d %H:%M')
        
        # Calculate the difference between exit and entry times in hours
        time_difference = (exit_time - entry_time).total_seconds() / 3600  # Convert seconds to hours
        total_hours += time_difference  # Add to the total hours worked

        # Check if the workday is in the list of extra pay days
        if entry_time.date().strftime('%Y-%m-%d') in extra_pay_days:
            # If it's a day with extra pay, calculate the extra pay for the hours worked on that day
            total_extra_pay += time_difference * hourly_rate * (extra_rate - 1)  # Extra pay for the worked hours

    # Calculate the total salary by multiplying total hours by the hourly rate
    total_salary = total_hours * hourly_rate
    # Add the extra pay to the total salary
    total_salary_with_extra = total_salary + total_extra_pay

    return total_hours, total_salary_with_extra, total_extra_pay  # Return total hours, total salary with extra, and extra pay

# Example usage
entries = [
    {'entry': '2024-11-01 09:00', 'exit': '2024-11-01 17:00'},  # Work entry and exit for Nov 1st
    {'entry': '2024-11-02 09:30', 'exit': '2024-11-02 18:00'},  # Work entry and exit for Nov 2nd
    {'entry': '2024-11-03 08:45', 'exit': '2024-11-03 16:45'}   # Work entry and exit for Nov 3rd
]

hourly_rate = 15.0  # Hourly rate in dollars
extra_pay_days = ['2024-11-02']  # Extra pay applies on Nov 2nd
extra_rate = 1.5  # Extra pay rate is 50% more for extra pay days

# Call the function to calculate hours and salary
total_hours, total_salary, total_extra_pay = calculate_hours_and_salary(entries, hourly_rate, extra_pay_days, extra_rate)

# Print the results
print(f"Total hours worked: {total_hours:.2f} hours")
print(f"Total salary: ${total_salary:.2f}")
print(f"Total extra pay: ${total_extra_pay:.2f}")
print(f"Total salary including extra pay: ${total_salary + total_extra_pay:.2f}")