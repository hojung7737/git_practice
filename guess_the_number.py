import random


#input for range   
a = int(input("Enter first range: "))
b = int(input("Enter second range: "))

#input random int from a to b
ran_value = random.randint(a,b)

run = True
count = 0
while(run):
  count += 1
  guess = int(input("Enter your guess "))
  if(guess < a or  guess > b):
    print("Warning: input value out of range.")
  elif(guess < ran_value):
    print("The answer is greater than", str(guess) + ".")
  elif(guess > ran_value):
    print("The answer is smaller than", str(guess)+".")
  else:
    print("Wow you guess the right number")
    run = False
  
print("number of guesses:", str(count))

