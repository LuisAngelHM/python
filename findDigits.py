'''Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.'''


def findDigits(n):
    count = 0
    for digit in str(n):
      if int(digit) != 0 and n % int(digit) == 0:
        count += 1
    return count

if __name__ == "__main__":

  for number in [12, 1012]:
    print(findDigits(number))
