## Fibonacci

## Haskell

40 bytes, 40 chars

```hs
f=0:scanl(+)1f
main=mapM print$take 31 f
```

## Python

47 bytes, 47 chars

```py
def A(i,j):print(i);i<832040 and A(j,i+j)
A(0,1)
```