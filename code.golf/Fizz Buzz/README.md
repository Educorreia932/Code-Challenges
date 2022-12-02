# Fizz Buzz

## Python

### Fewest bytes

59 bytes, 59 chars

```py
for A in range(100):print(A%3//2*'Fizz'+A%5//4*'Buzz'or-~A)
```