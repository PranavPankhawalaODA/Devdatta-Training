def square_root(x):
    if x<0:
        raise ValueError("Cannot compute square root of negative number")

    guess = x / 2.0
    epsilon = 0.00001

    while abs(guess*guess - x) >= epsilon:
        guess = (guess + x / guess) / 2.0

    return guess

def main():
    try:
        number = float(input("Enter a number to compute its square root: "))
        result = square_root(number)
        print(f"The square root of {number} is approximately {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()