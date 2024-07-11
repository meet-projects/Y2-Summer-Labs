# IASA Weather Report Script

In this lab, we will be reviewing conditionals, loops, and lists by creating a Python script to generate a weather report for the week. This script will:

- Generate a list of random temperatures for each day of the week.
- Determine which days have even temperatures (good days for Shelly).
- Identify the hottest and coldest days of the week.
- Calculate which temperatures are above average.


## Instructions

1. **Create a Python File**
    - Create a file named `python_review.py`.

2. **Generate Random Temperatures**
    - Create an empty list called `temperatures`.
    - Fill the list with exactly 7 random temperatures between 26-40 using the `random` library.
    - The index of the list represents the day of the week:
        - 0: Sunday
        - 1: Monday
        - 2: Tuesday
        - 3: Wednesday
        - 4: Thursday
        - 5: Friday
        - 6: Saturday

3. **Shelly's Good Days**
    - Count the number of days with even temperatures.
    - Print the days that have even temperatures.
    - Create a variable `good_days_count` to store the number of good days.

4. **Ibrahim's Hot Days**
    - Find the highest and lowest temperatures of the week.
    - Save the highest temperature and the corresponding day to `highest_temp` and `highest_temp_day`.
    - Save the lowest temperature and the corresponding day to `lowest_temp` and `lowest_temp_day`.

5. **Above Average Temperatures**
    - Calculate the average temperature of the week.
    - Create a list called `above_avg` to store temperatures above the average.

6. **Print the Report**
    - Print a report with the following information:
        - Temperatures for the week.
        - Good days for Shelly.
        - The highest and lowest temperatures and their respective days.
        - The average temperature.
        - Days with temperatures above the average.
    - It should look something like this:

   - <img src="https://raw.githubusercontent.com/meet-projects/Y2-Summer-Labs/master/2.1%20python%20review%20%231/temp%20report.jpg" width="670" height="530">

## Bonus task!
create a new a list call it **`sorted_temp`**,
sort out the temprtures from lowst to highest inside the `sorted_temp`.
print the temprtures from lowest to highest.