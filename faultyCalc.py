num1 =(int)(input("Enter the number :"))
num2 =(int)(input("Enter the another number :"))
Selection = input("Enter options from given below -\n 1.  +\n 2.  - \n 3.  *\n 4.  /\n 5.  %\n 6.  //\n 7.  **\n ") 
if ((num1 == 45) and (num2 == 3)):
      print("555")
elif ((num1 == 100) and (num2 == 45)):
    print("0")
elif ((num1 ==1) and (num2 == 0)):
    print("none")         
else:
    
 def add():
     return (num1+num2)

 def subtract():
     return (num2-num1)

 def  multiply():
     return (num1*num2)

 def divide():
     return (num2/num1)    

 def modulo():
     return (num2%num1)

 def floorDivision():
     return(num2//num1)

 def expopower():
     return (num2**num1)


if Selection == '1':
     print(add())
elif Selection == '2':
     print(subtract())
elif Selection == '3':
     print(multiply())
elif Selection == '4':
     print(divide())
elif Selection == '5':
     print(modulo())
elif Selection =='6':
     print(floorDivision())
elif Selection == '7':
     print(expopower())                             
else:
     print("No selection")  

 