import operation


def main():
    print('Calculator App')
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))

    print(f'Addition: {operation.add(num1, num2)}')
    print(f'Subtraction: {operation.subtract(num1, num2)}')
    print(f'Multiplication: {operation.multiply(num1, num2)}')
    print(f'Division: {operation.divide(num1, num2)}')


if __name__ == "__main__":
    main()
    while True:
        pass
