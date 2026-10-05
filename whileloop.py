#1.Find the sum of digits in a given number.
    #Example: 738 → 7 + 3 + 8 = 18
sum=0
n=int(input("Enter a Number: "))
while(n > 0):
    digit=n % 10
    sum = sum + digit
    n = n // 10
print(sum)
#_____________________________________________________________________________________________________________________________________#
#2..Find the average of digits in a given number.
     #Example: 624 → (6 + 2 + 4) / 3 = 4
sum=0
num=int(input("Enter a Number: "))
count=0
while num > 0:
    digit=num % 10
    sum = sum + digit
    count= count+1
    num=num // 10
avg=sum/count
print(avg)
#______________________________________________________________________________________________________________________________________#
#3..Find the sum of the first digit and the last digit of a given number.
     #Example: 936 → 9 + 6 = 15
num = 936
last_digit = num % 10
while num >= 10:
    num = num // 10
first_digit = num
sum = first_digit + last_digit
print(sum)
#_________________________________________________________________________________________________________________________________________#
#4.Find the average of digits that are divisible by 5 in a given number.
    # Example: 12575 → Divisible by 5 digits: 5, 5, 5 → Average = (5 + 5 + 5) / 3 = 5
num = 12575
sum = 0
count = 0

while num > 0:
    digit = num % 10

    if digit % 5 == 0:
        sum = sum + digit
        count = count + 1

    num = num // 10

average = sum / count

print(average)
#_____________________________________________________________________________________________________________________________________________#
#5.Find the difference between the largest digit and the smallest digit in a given number.
#  Example: 58321 → Largest = 8, Smallest = 1 → Difference = 8 - 1 = 7
num = 58321
largest = 0
smallest = 9

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    num = num // 10

difference = largest - smallest

print(difference)
#______________________________________________________________________________________________________________________________________#

