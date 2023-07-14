# Divisors

## Python

### Fewest bytes

64 bytes, 64 chars

```py
for A in range(1,101):print(*[B for B in range(1,A+1)if A%B<1])
```
