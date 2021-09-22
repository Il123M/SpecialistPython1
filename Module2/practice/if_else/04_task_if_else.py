# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here
number = int(input("Введите число: "))
a=number%3
b=number%5
if a==0:
 if b==0:
  print ("FOOBAR")
 else:
    print ("BAR")
elif b==0:
    print ("FOO")
else:
    print ("NONE")
