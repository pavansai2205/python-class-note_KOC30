age=input("enter your age:")
age=int(age)
if age>=18:
    print("your adult")
else:
    print("your not a adult") 

age=int(input("enter your age :"))
if age>=18:
    print("your are adult")
else:
    print("your are child") 

winning_number = 25
user_input = input("guess a number b/w 1 and 100 : ")
user_input = int(user_input)
if user_input == winning_number:
  print("You win !!!")
else:
    if user_input < winning_number:
      print("too low")
    else:
      print("too high")          


name="pavansai"
age=18
if name=="pavansai" and age==18:
    print("true")
else:
    print("false")

user_name = input("enter your name place:")
user_age=input("enter your age:")
if user_age >=10 and (user_name[0])=='a' or (user_name[0]=='A'):
    print("you  can watch coco")
else:
    print("you can watch coco") 

#elif statments:   
age = input("please input your age : ")
age = int(age)
if 0<age<=3:
  print("Ticket price : Free")
elif 3<age<=10:
  print("Ticket price : 150")
elif 10<=age<=60:
  print("Ticket price : 250")
else:
  print("Ticket price : 200")


#while statments 
i=1
while i <10:
    print("hello world")
    i=i+1

total=0
i =1 
while i <=10:
    total = total + i 
    i+=1
print(total) 


n = input("enter a number : ")
n = int(n)
total = 0
i = 1
while i <= n:
  total += i
  i += 1
print(total)

i=0 
while i <=10:
    print("pavansai")
    i+=1

#for loop
for i in range(10):
    print(f"pavansai:{i}")    