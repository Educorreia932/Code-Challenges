def principal_period(s):
    i = (s + s).find(s, 1, -1)
    
    if i == -1:
        return None  

    else:
        return i

N, T = [int(x) for x in input().split(" ")]

lights = ["0" for i in range(T)]

for x in input().split(" "):
    lights[int(x) - 1] = "1"

lights = "".join(lights)
period = principal_period(lights)

if period == None:
    print(T - 1)

else:
    print(period - 1)