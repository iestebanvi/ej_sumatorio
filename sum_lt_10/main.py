#!/bin/python3
import random

def check_sum (num1,num2,result):
  resultado=num1+num2
  print (resultado)

  if (num1+num2) == result:
    return True
  else:
    return False

inputVal=''

while inputVal != 'quit':
  num1=random.randint(0, 12)
  num2=random.randint(0, 12)
  print (f""" Cuanto suman los numero
    {num1}
  +
    {num2}
  ----------
  """)
  try:
    result=int(input())
    if check_sum (num1,num2,result):
      print (True)
    else:
      print (False)
  except:
    print ("Error en el numero introducido")
    if result == "quit":
      exit()  

