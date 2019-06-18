def isPrime(start):
    for i in range(2, start):
        if(start % i == 0):
            return 0
    return 1
def sumIsOdd(start):
    result = 0
    for i in str(start):
        result = result + int(i)
    if (result % 2 == 0):
        print "sum is not prime" 
        return 0
    else:
        return 1

first = 1000000 # 1 million
cnt = 0
solve = [0]
while (1):
    print first
    if(isPrime(first)):
        if (sumIsOdd(first)):
            cnt += 1
            solve.insert(cnt, first)
            print "Find! "
            if(cnt == 2):
                break
    first += 1

print "=========================================s"
print solve[1]
print solve[2]
print "Answer is "+str(solve[1])+str(solve[2])
