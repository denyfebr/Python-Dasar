# operasi logika atau boolean

# not, or, and, xor

# NOT
print('====NOT====')
a = True
c = not a
print('data a =',a)
print('---------NOT')
print('data c =',c)
print('\n')
# OR
print('====OR====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

print('====OR====')
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

print('====OR====')
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

print('====OR====')
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)
print('\n')
# AND
print('====AND====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

print('====AND====')
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

print('====AND====')
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

print('====AND====')
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

print('\n')
# XOR
print('====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

print('====XOR====')
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

print('====XOR====')
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

print('====XOR====')
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)