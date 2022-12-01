# a=int(input("Enter any number: "))
# b=int(input("Enter any number: "))
# c=int(input("Enter any number: "))
# d= a+b+c
# print(f"Average is {d/3}")
a, b, c= input("Enter any three numbers separted by comma: ").split(",")
print(f"Average of three numbers : {(int(a)+int(b)+int(c))/3}")