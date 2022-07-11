#!/bin/python3
import random

def check_sum (num1,num2,inputVal):
  if (num1+num2) == inputVal:
    return True
  else:
    return False

inputVal=''
npoints=0
nfails=0


while inputVal != 'quit':
  num1=random.randint(0, 12)
  num2=random.randint(0, 12)

  print (f"""Para salir, escribir 'quit'. 
  Cuanto suman los numeros
    {num1}
  +
    {num2}
  ----------
  """)
  
  inputVal=input()

  if inputVal == 'quit':
    print ("Hasta Luego...!!")
    print ("")
    exit()
  else:
    try:
      inputVal=int(inputVal)
      if check_sum (num1,num2,inputVal):
        print ("Correcto!!")
        npoints+=1
        print (f"Puntos acumulados: {npoints}")
        print (f"ERRORES: {nfails}")
      else:
        print (f"Ohh, fallo. La suma son {num1+num2} Puntos acumulados: {npoints}")   
        nfails+=1
    except:
      print ("Error en el numero introducido")


