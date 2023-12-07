# Integer

# ? 24
def get_weekday(number):
    match number:
        case 0:
            print("sunday")
        case 1:
            print("monday")
        case 2:
            print("tuesday")
        case 3:
            print("wednesdat")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("saturday")
        case _:
            return "Default case"


k = int(input("целое число K,лежащее в диапазоне 1-365:"))
n = (k - 1) % 7
get_weekday(n)
