#create empty list to store binary number
binaryL = []

#create recursive function to turn decimal into function
def toBinary(num):
  #if num 
  if num == 1:
    binaryL.append(1)
    return 1
  
  #if number != 1, call the function again to reduce num value
  else:
    binaryL.append(num % 2)
    return (toBinary(num // 2 ))

#get user input
x = int(input())

#call the function, using user input
toBinary(x)

#create new empty list to store decimal number
decimalL = []

#create function to turn binary to decimal
def toDecimal(b_list):
  
  #create variable that equals 0
  value = 0

  for i in range(len(b_list)):
    #pop each digit from binaryL
    digit = b_list.pop()
    
    #if digit is equal to 1, 
    if digit == 1:
      value = value + pow(2, i)
  print(value)

toDecimal(binaryL)
