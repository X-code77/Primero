import random 
barcox = str(random.randint(0,1))
barcoy = str(random.randint(0,1))


jugadorx= input("por favor introduzca un numero")

jugadory= input("por favor introduza otro numero")

if (jugadorx == barcox and jugadory == barcoy ):
   print("win")
else:
   print("lose")



    
