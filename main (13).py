#DEBUGGED CODE:
for number in range(1, 101):
  if number % 3 == 0:
    if number % 5 == 0:
      print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

#BUGGED CODE:
#for number in range(1, 101):
  #if number % 3 == 0 or number % 5 == 0:
    #print("FizzBuzz")
  #if number % 3 == 0:
    #print("Fizz")
  #if number % 5 == 0:
    #print("Buzz")
  #else:
    #print([number])