## Fizz Buzz

## Python

34 bytes, 34 chars

```py
for A in range(1,101):print(('Fizz','')[A%3>0]+('Buzz','')[A%5>0]or A)
```