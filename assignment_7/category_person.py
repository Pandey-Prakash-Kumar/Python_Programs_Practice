age = int(input("Enter your age:"))

match age:
    case age if age < 10:
        print("Kid")
    case age if age < 20:
        print("Teen")
    case age if age < 40:
        print("young")
    case age if age < 60:
        print("Experienced")
    case age if age <= 60:
        print("Senior Citizen")