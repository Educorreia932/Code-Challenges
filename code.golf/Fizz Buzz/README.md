## Fizz Buzz

## Python

62 bytes, 62 chars

```py
for A in range(1,101):print('Fizz'*(A%3<1)+'Buzz'*(A%5<1)or A)
```