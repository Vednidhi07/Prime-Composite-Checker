''' In This project we have to enter a positive integer range[A,B] and system will find out the status
(prime or composite)of each number available in the given range.At the end point the count also. '''

a = int(input(">>>Enter start range: "))
b = int(input(">>>Enter end range: "))
print("___________________________\n")
count_prime = 0
count_composite = 0
if a>1 and a<b:
    for i in range(a, b+1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count = count+1
        if count>0:
            count_composite += 1
            print(i,"is a Composite Number")
        else:
            count_prime += 1
            print(i,"is a Prime Number" )
    print(f"\nThere are total of {count_prime} prime numbers, and {count_composite} composite numbers in the given range")
elif(a==1 and a<b):
    print("1 is neither prime nor composite")
    for i in range(a+1, b+1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count = count+1
        if count>0:
            count_composite += 1
            print(i,"is a Composite Number")
        else:
            count_prime += 1
            print(i,"is a Prime Number" )
    print(f"\nThere are total of {count_prime} prime numbers, and {count_composite} composite numbers in the given range")

else:
    print("Enter the positive number")
