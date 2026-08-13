#Match Expression

day = 4 
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3 :
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5 :
        print("Friday")
    case 6 : 
        print("Saturday")
    case 7 :
        print("Sunday")

# Default Value

days = 4
match days:
    case 6 : 
        print("Today is Saturday")
    case 7 :
        print("Today is sunday")
    case _:
        print("Looking forward to the weekend")


days = 4

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7 :
        print("I love weekend")


month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A wwekday in April")
    case 1 | 2 | 3| 4| 5 if month == 5 :
        print("A weekday in May")
    case _:
        print("No Match")