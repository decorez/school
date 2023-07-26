import sys

number = int(input("input your number : "))

if number < 0:
    sys.exit('your number is negative')
elif number > 0:
    print('your number is positive')
elif number == 0:
    print('your number is zero')
print ('thank you')
sys.exit(0)