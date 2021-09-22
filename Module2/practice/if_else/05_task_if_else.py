# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here
m = int(input("Введите число от 1 до 12: "))
if m==1:
 print ("January")
elif m == 2 :
  print ("February")
elif m == 3:
  print ("March")
elif m == 4:
  print ("April")
elif m == 5:
   print ("May")
elif m==6:
   print ("June")
elif m==7:
   print ("July")
elif m==8:
   print ("August")
elif m==9:
   print ("September")
elif m==10:
   print ("October")
elif m==11:
   print ("November")
elif m==12:
  print ("December")
