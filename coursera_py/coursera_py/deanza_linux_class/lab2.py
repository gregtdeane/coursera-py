# Gregory Tuayev-Deane
# Finds the insurance rate for an applicant based on age and 
# accident history. 
# Additionally, find the min, max, total price of the 3 cars
# and store values in a dictionary

age = int(input("Enter your age in years: "))
accident_hist = input("Enter 'yes' if you have ever had an accident, and 'no' if not: ")

if age<16:
    print("You're too young to drive! ")
elif age > 16 and age< 25:
    if accident_hist.lower() == "no":
        rate=3000
    elif accident_hist.lower() == "yes":
        rate=3500
elif age > 26 and age< 45:
    if accident_hist.lower() == "no":
        rate=2000
    elif accident_hist.lower() == "yes":
        rate=2500
elif age > 46:
    if accident_hist.lower() == "no":
        rate=1200
    elif accident_hist.lower() == "yes":
        rate=1500

print("Your insurance premium is: $", rate)

car1_val = float(input("Enter the 1st car's value in dollars: "))
car2_val = float(input("Enter the 2nd car's value in dollars: "))
car3_val = float(input("Enter the 3rd car's value in dollars: "))
car_val_list = [car1_val, car2_val, car3_val]


max_val = max(car_val_list)
min_val = min(car_val_list)
range_val = max_val-min_val
total_val = sum(car_val_list)

car_dict = {"max":max_val, "min":min_val, "range":range_val, "total":total_val}
print(car_dict)
