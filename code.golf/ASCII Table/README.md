## ASCII Table

## Python

120 bytes, 120 chars

```py
C=print
B=range
C('  ',*B(2,8),'\n','-'*13)
for A in B(16):C('%X:'%A,*['DEL'if A+C==22 else chr(C*16+A)for C in B(2,8)])
```
