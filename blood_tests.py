def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return

def getData():
    print("Enter HDL level: ")
    userInput = input()
    return userInput


def HDL_driver():
    # Get Data
    data = getData()

    # Analyze Data

    # Output Data

interface()
