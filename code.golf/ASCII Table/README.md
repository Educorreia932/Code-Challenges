## ASCII Table

## Python

114 bytes, 114 chars

```py
C=print
B=range(2,8)
C('  ',*B,'\n','-'*13)
for A in range(16):C('%X:'%A,*[('DEL',chr(C*16+A))[A+C<22]for C in B])
```
