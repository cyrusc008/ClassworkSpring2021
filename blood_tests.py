def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        if choice == "1":
            HDL_driver()

def getData():
    print("Enter HDL level: ")
    userInput = input()
    return userInput

def analyzeData(data):
    if int(data) >= 60:
        print("Normal")
    elif (int(data) >= 40) & (int(data) < 60):
        print("Borderline Low")
    else:
        print("Low")

def HDL_driver():
    data = getData()
    analyzeData(data)

interface()
