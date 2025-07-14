#int:
#note: int is immutable.
#it can store the sam evalue in another memory block

import sys
x = 101
y = -15
p = 123456789012345

print(x)
print(y)

import sys
sys.getsizeof(x)

e = 102
print(id(e))
e = 201
print(id(e))


#float
#declaration and initialization
#floating point representation
# ex1:

# a = 12500
#  125*100
# 125*10^2
# 125*E2
# 125 E2
# mantissa   exponent

###example2
# b = 23.45
# 2345/100
# 2345/10^2
# 2345*10^-2
# 2345*E-2
# 2345 E-2

#examples

# a = 12.3
# b = -23.4
# c = 123E2
# d = -123E-2
# print(a,b,c,d)

# 12.3 -23.4 12300.0 -1.23

##BOOLEAN Datatype
#bool is a integral value(True =1, False =0)
#booleans are used on conditions[ex: a = 5,b = 2; a>b --> True; if a>b:]
# x = True
# y = False
# print(x,y)
# int(x)
# type(x)

# a = 10
# b = 5
# a > b

# True False
# True

#complex datatype
#a + bj
#c1 = a + bj
# c2 = 5 + 3j
# c3 = 2.5 + 1.5j
# c4 = complex(2.5,1.5)
# c = complex(10)
# print(c2,c3,c4,c)

# (5+3j) (2.5+1.5j) (2.5+1.5j) (10+0j)
