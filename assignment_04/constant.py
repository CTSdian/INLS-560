MIN_SALES_YEARS = 3
MIN_TOP_REWARDS = 2

def congrats():
    print("Congrats! You are eligible for Sales Manager.")

sales_years = int(input("Your years of sales experience:"))
top_years = int(input("How many years have you winned the SALESPERSON OF THE YEAR:"))

flag = True
while flag:
    if(top_years > sales_years):
        print("Invalid input. Please enter years of SALESPERSON OF THE YEAR again.")
        top_years = int(input("How many years have you winned the SALESPERSON OF THE YEAR:"))
        if(top_years <= sales_years):
            flag = False
    else:
        flag = False

if sales_years >= MIN_SALES_YEARS:
    if(top_years >= MIN_TOP_REWARDS):
       congrats()
    else:
        print(f"""
You are not eligible for Sales Manager,
because you still need to win {MIN_TOP_REWARDS - top_years} more SALESPERSON OF THE YEAR.
              """)
else:
    word = 'years'
    if(MIN_SALES_YEARS - sales_years == 1):
        word = 'year'

    if(top_years >= MIN_TOP_REWARDS):
        print(f"""
You are not eligible for Sales Manager,
because you still need {MIN_SALES_YEARS - sales_years} more {word} of experience.          
            """)
    else:
        print(f"""
You are not eligible for Sales Manager,
because you still need {MIN_SALES_YEARS - sales_years} more {word} of experience.
Besides, you also need to win {MIN_TOP_REWARDS - top_years} more SALESPERSON OF THE YEAR.  
            """)