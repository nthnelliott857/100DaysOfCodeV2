

def test(num1):
    num2 = 5
    while num1 != num2:
        if num1 > num2:
            return "num1 > num2"
        elif num2 > num1:
            return "num2 > num1"
        else:
            return "num1 = num2"

print(test(input("")))