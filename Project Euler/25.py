# 1000-digit Fibonacci number

i = 2
f1 = 1
f2 = 1

while True:
    if len(str(f1)) == 1000:
        break
    
    f = f1 + f2
    f2 = f1
    f1 = f

    i += 1

answer = i

print(answer)

