# takes a parameter 'n' and returns true if number cannot be divided
def isPrime(n):
    # check if n is only divisible by itself
    for i in range(2,n):   
        if n % i == 0:
            return False;
    return True;
    
# takes a number as parameter and returns all numbers that are prime numbers
# up to the provided number parameter
def getPrimeNumbers(n):
    #initialize list
    primeNums = [];
    # start from 2 iterate all the way to n
    for i in range(2, n+1):
        if(i == 2):
            # append 2
            primeNums.append(2);
        else :
            if(isPrime(i)):
                # if factor is found, add number to list
                primeNums.append(i);
    return primeNums;
    

    
