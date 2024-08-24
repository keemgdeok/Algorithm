N=int(input())

for i in range(N-1):
    for _ in range(N-i-1):
        print(" ", end="")
    print("*", end="")
    
    for _ in range(i*2-1):
        print(" ", end="")
    
    if i > 0: print("*", end="")

    print()

for _ in range(2*N-1):
    print("*", end="") 