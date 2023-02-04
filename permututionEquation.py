def permutuationEquation(p):
  return [ p.index(p.index(number)+1)+1 for number in range(1, max(p)+1)]


if __name__ == "__main__":
  print(permutuationEquation([4, 3, 5, 1 ,2]))