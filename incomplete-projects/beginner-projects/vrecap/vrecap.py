#comments
x= 'y' #comments can be used anywhere after a line of code
"""you can also document/ comment out like this
this is a multi line string. people use it for multi line strings but you can also use 
it this way. python will ignore it if you do not assign a variable to it."""
#variables
var1 = int(3)
var2 = str(3)
var3 = float(3)

print(var1)
print(type(var2))
print(var3)

a = 'a'
A = 'A'
myvar = 0
mYvar = myvar
myvar1 = 0
print(myvar1)
MyName = 0 #pascal case
myName = 0 #camelcase
my_name = 0 # snake case

p, y, i = 4, 'yes', True
print(p)
print(y)
print(i)

aa = aaa = v7 = "Im gay"
print(aa)
print(aaa)
print(v7)
#unpack --
list = ['I', 'Love', "You"]
f, r, y = list
print(f)
print(r)
print(y)
#or

print(f, r, y) # (f + r + y)

try:
    global g  # we do this, so we can call g, o
    global o  # because g and o are out of our scope, it is declared ina n indent and we are after the indent
    # but we should use functions or loops instead, dont use global ()
    g = 7
    o = 'days till i win'
    print(g + o)
except Exception as e:
    print(e)

print(g, o)

listh = [7, 9 , 2, 40]
print(listx)