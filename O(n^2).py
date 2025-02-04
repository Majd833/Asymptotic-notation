def onsquare(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
            iteration+=1
        print(" ")
    print("\n the value of n is ",n,"the number of iterations is ",iteration)
onsquare(5)
onsquare(4)
onsquare(7)