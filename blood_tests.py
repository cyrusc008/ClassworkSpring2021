def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()

def getData():
    print("Enter HDL/LDL level: ")
    userInput = input()
    return userInput

def outputResults(analysis):
    print(analysis)

def analyzeHDL(data):
    if int(data) >= 60:
        result = "Normal"
    elif 40 <= int(data) < 60:
        result = "Borderline Low"
    else:
        result = "Low"
    return result

def analyzeLDL(data):
    if int(data) < 130:
        return "Normal"
    elif 130 < int(data) < 159:
        return "Borderline High"
    elif 160 < int(data) < 189:
        return "High"
    else:
        return "Very High"

def HDL_driver():
    data = getData()
    analyzeHDL(data)

def LDL_driver():
    data = getData()
    analysis = analyzeLDL(data)
    outputResults(analysis)

if __name__ == "__main__":
    interface()
