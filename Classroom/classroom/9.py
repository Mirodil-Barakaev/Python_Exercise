while True:
 amal = input("Amal kiriting '+' '-' '/' '*' yoki 'q' kiriting chiqib ketish uchun: ")
 if amal == 'q':
    print("Dastur tugadi")
    break
 a = int(input("1 son kiriting: "))
 b = int(input("2 son kiriting: "))
 

 if amal == "+":
  print(a+b)
 elif amal == "-":
  print(a-b)
 elif amal == "/":
  print(a/b)
 elif amal == "*":
  print(a*b)  
 else:
  print("Notogri amal kiritingiz!!")





