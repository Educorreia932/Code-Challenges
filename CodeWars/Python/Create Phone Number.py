def create_phone_number(n):
    _n = "".join(str(x) for x in n)
    
    return f"({_n[0:3]}) {_n[3:6]}-{_n[6:]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
