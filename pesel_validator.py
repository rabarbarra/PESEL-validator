
def check_gender():
    if int(pesel[9]) % 2 == 0:
        print("Gender: Female")
    else: 
        print("Gender: Male")

def check_pesel():
    while True:
        try:
            global pesel
            pesel = input("Enter your PESEL: ")
            sum = 1*int(pesel[0]) + 3*int(pesel[1]) + 7*int(pesel[2]) + 9*int(pesel[3]) + 1*int(pesel[4]) + 3*int(pesel[5])+ 7*int(pesel[6]) + 9*int(pesel[7]) + 1*int(pesel[8]) + 3*int(pesel[9]) + 1*int(pesel[10])
            if sum % 10 == 0:
                print("Your PESEL number is correct :)")
                check_gender()
                break
            else:
                print("Incorrect PESEL!")
        except ValueError:
            print("It looks like you entered letters. Enter numbers only.")
        except IndexError:
            print("Please enter an 11-digit number.")

check_pesel()


def date_of_birth():
    month_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Nov", "Oct", "Dec"]
    day = pesel[4:6]
    month_check = int(pesel[2:4])
    if month_check > 20:
        century = 2000
        month_check -= 20
    else: 
        century = 1900
    month = month_name[month_check - 1]
    year = century + int(pesel[0:2])
    print(f"You were born on {day}th of {month} {year}")

date_of_birth()
