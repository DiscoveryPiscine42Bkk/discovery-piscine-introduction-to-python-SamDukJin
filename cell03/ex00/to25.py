num_inp = int(input("Enter a number less than 25: "))

if num_inp < 25 :
   for i in range(num_inp, 26) :
      print("Inside the loop, my variable is : ", i)

elif num_inp > 25:
   print("Error")