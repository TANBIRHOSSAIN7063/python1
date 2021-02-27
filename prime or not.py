


# using python caculate a number prime or not


def factorial(n) : 

    fact = 1

    while (n != 0) : 

        fact = fact * n 

        n = n - 1

    return fact 

def isKrishnamurthy(n) : 

    sum = 0

    temp = n 

    while (temp != 0) : 

  
        rem = temp%10

        sum = sum + factorial(rem) 

        temp = temp // 10

          

    return (sum == n) 

  


n = int(input("Enter any number"))

if (isKrishnamurthy(n)) : 

    print("YES") 

else : 

    print("NO") 