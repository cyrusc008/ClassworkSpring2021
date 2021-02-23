def function_error(x, y):
    try:
        print(x / y)
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except TypeError:
        print("Make sure you entered two numbers")


def main():
    function_error(5, 0)
    function_error(5, "a")


if __name__ == "__main__":
    main()
