## Fibonacci

## Haskell

```hs
f=0:scanl(+)1f
main=mapM print$take 31 f
```

## Python

53 bytes, 53 chars

```py
for A in range(31):print(int(1.61803398**A/5**.5+.5))
```