literal/constant/data
___________________________
integer       10,-5,57
floating ponit/real   3.5,-4.7
string               'a' "a"   '''a''' """a"""  "123"
bool                  True  False
complex              3+2j  4-5j

5
5.0
'5'
"5"
5+0j

print(): it is predefined function.
it is used display output

#wap display any integer real  and string

print(5)
print(7.8)
print("hi")


escape  sequence
_____________________
\n
\t
\b
\r
\\



#wap display any integer real  and string
print(10,3.7,"hi")

by default
________________
print(sep=" ",end="\n")




print("hi\nram")

o/p:
hi
ram

print("hi\tram")
o/p:
hi   ram



print("hi\bram") #hram
print("hi\b\bram") #ram
print("hi\rram") #ram
print("hello\bindia") #hellindia
print("hello\rindia") #ind


identifier
______________
it is user defined word.
This word is used to give name of the variable clasname ,.....

rule
______
(1)it consist of
 a to z
A to Z
0 to 9
_

(2)not start with digit

(3)space not allow
(4)case senistive  a!=A
(5) predefined word not allow

import keyword
print(len(keyword.kwlist))
print(keyword.kwlist)

35
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


identify the identifier
________________________
abd   v 
aBd   v
a3    v
3a    iv
a$B   iv
a_b    v
_ab   v
a b    iv
if     iv
IF     v  (not recommand)


datatype:
it tell the compiler your variable store which type data

inbulit datatype
______________________ (immutable)
int
float
str
bool
complex

other datatype
_______________
list
tuple
set
dict


variable:
it is memeory location name.
where store and retrive data.

How to initize variable in c c++ java
_____________________________________________
datatype variablename;
varaiablename=literal;


in python
______________
variablename=literal
a=10
b=2.5



a=10
b=2.5
print(a,b)


type():
it is predefined function.it is used check your variable or literal which type.
a=10
b=2.5
c="hi"
print(type(a))
print(type(b))
print(type(c))
print(type(True))

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

id():it is predeined function .it is used to show refernce or address variable, literal.

a=10
b=2.5
print(id(a),a)
print(id(b),b)

140720976300760 10
2000900959344 2.5


single line intlization
____________________________
a=10
b=2.5
c="hi"

or

a,b,c=10,2.5,"hi"
print(a,b,c)


o/p:
10 2.5 hi


a=10,2.5,"hi"
print(type(a),a)

o/p:
<class 'tuple'> (10, 2.5, 'hi')


grammer
_______________
a=10
print("hi ram")
print("a")
print(a)



o/p:
hi ram
a
10


a=20
print("a")
print(a)
print("a+3")
print(a+3)


o/p:
a
20
a+3
23



a=10
b=20
print("first no=",a)
print("second no=",b)
print("add=",a+b)
print("mult=",a*b)

o/p:
first no=10
second no=20
add=30
mult=200



or
a=10
b=20
print("first no=",a)
print("second no=",b)
s=a+b
print("add=",s)
m=a*b
print("mult=",m)






print("enter two nos ")
a=int(input())
b=int(input())
print("first no=",a)
print("second no=",b)
s=a+b
print("add=",s)
m=a*b
print("mult=",m)


o/p:
C:\Users\LENOVO\OneDrive\Desktop\python9pm>py test.py
enter two nos
10
20
first no= 10
second no= 20
add= 30
mult= 200

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py test.py
enter two nos
50
60
first no= 50
second no= 60
add= 110
mult= 3000

input()
____________
it is a predefined function take input from keyboad in program runtime.
by default it takes string type.

#wap take string from keyboad and display it
print("enter a string ")
nm=input()
print("vaule=",nm)

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string
muna das
vaule= muna das

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string
kuna das
vaule= kuna das


input() : it take one argument that must be string type.

#wap take string from keyboad and display it
nm=input("enter a string ")
print("vaule=",nm)

o/p:

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string muna
vaule= muna
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string kuna
vaule= kuna



#wap take string from keyboad and display it
nm=input("enter a string\n")
print("vaule=",nm)



#wap take two integer from keyboad and add it
print("enter integer number ")
no1=input()
print("enter another integer number ")
no2=input()
s=no1+no2
print("sum=",s)

o/p:
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter integer number
10
enter another integer number
20
sum= 1020



#wap take two integer from keyboad and add it
print("enter integer number ")
no1=int(input())
print("enter another integer number ")
no2=int(input())
s=no1+no2
print("sum=",s)


"""
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter integer number
10
enter another integer number
20
sum= 30

"""


print("enter rectangle length and breadth")
L=int(input())
B=int(input())
print("length=",L)
print("breadth=",B)
ar=L*B
print("area=",ar)
pr=2*(L+B)
print("perimetr=",pr)


o/p:
enter rectangle length and breadth
7
8
length= 7
breadth= 8
area= 56
perimetr= 30





#wap take student name rollno mark keyboad  and dispaly it
print("enter name rollno and mark ")
nm=input()
r=int(input())
m=float(input())
print("name=",nm)
print("rollno=",r)
print("mark=",m)

"""
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter name rollno and mark
m das
1
90.50
name= m das
rollno= 1
mark= 90.5
"""



print(pow(2,3))
import math
print(pow(2,3))
print(math.pi)
print(math.pow(2,3))



wap take a student 4 mark from keyboad dispaly all mark
totalmark and avaerage mark

wap take square side formkeyboad dsipaly side area and perimeter

wap take circle radius from keyboad display radius arae and perimetr


convert to f  to c

conver c to f

wap find the simple interset

wap take eme sarly from keyboad  da=30% hra=20% then
display basic sal da hra and total sal







operator
_________

operator is a symbole that operate the operand.
operand may be varibale constant and expression

unary operator :
it operates one operand .
-5

binary operator :
it operates two operand:
a+b
5*6

ternary operator :
it operates three operand.
in python no ternary operator

?   :

precdence:
it is a table.
it decide which operator evaluate first.

associtive:

more than operator same precdence 
same operator more than in expression
it may be evalute 

left to right 
right to left

*  /  %  //  2  L to R
+ -         3

arithmethic operator
_________________

**  power           10**3    1000      precdence  2     right to left
/   exactly division  10/3     3.33333   precedence 3     Left to right
//  floor  division  10//3    3            "                 "
%    module            10%3    1          "                   "
*     mult              10*3   30         "                  "
+     binary plus       10+3   13         precedence 4       "

-     binary  plus      10-3     7           "               "

unary + -    precdence    2      


precdence
_____________
10+3*2**3


10+3*8
10+24
34


Left to right
_________

10//3*5%2
3*5%2
15%2
1


10*3//4*2
30//4*2
7*2
14



right to left
____________

2**3      
8


2*3*2    
2**9
512




10+5//2
12


10+5/2
12.5






display first digit
_____________________

1258//1000      1
476//100        4
34//10            3
56//10              5

display last digit
_____________________

1258%10     8
476%10       6
34%10       4
56%10       6



last digit delete

_____________________
1258//10      125
476//10       47
34//10        3
56//10         5


a=3
b=10
c=2
a=a+4
b=b//c
c=a+b
print(a,b,c)


o/p:

7 5 12


a=3
b=10
c=2
a=a+4
b=b//c
a+b
print(a,b,c)
o/p:
7 5 2


a=3
print(a+2)
print(a)

o/p:
5
3

a=3
a=a+2
print(a)

o/p:
5


a=3
print(a=a+2)
print(a)

o/p:
error

valid in java c,c++
5
5

unary + - operator
________________

a=5
b=-a
print(a,b)
o/p:
5 -5


add two no without using + operator
________________________________
a=5
b=7
c=a- -b
print("sum=",c)


o/p:
12


increment(++) and decrement(--) operator not avaliable in python.


a=5
++a
print(a)

o/p:
5

in java  c, c++
o/p:
6


a=5
a=a+1
print(a)
o/p:
6


a=5
a+=1
print(a)
o/p:
6



relation operator
_____________
<    lessthan
>    greaterthan
<=   lessthanequal
>=
==   is equal
!=

after compare result true or false

3<5    True
3>5     False
3<=3    True
2<=3    True
4<=3     False
3>=3     True
4>=3  True
4>5    False
3==3     True
3==4     False
3!=4       True

10<20<30    True                    in java error

10<50<30    False

2<3==3>2    True   


print(2<3==3>2)
print(2<3==5>2)

True
False


logical or short circut operator
_________________________________
combine two realtion operator
or   
and 
not

    or 
op1     op2      result
True    True      True
True    False     True
False    True     True
False    False     False

print(True or False)  #True

if first operand is true  second operand not checking.
if first operand  is false  second operand must checking
any nonzero value    true 

3 or 5    3  print(3 or 5)
0 or  5   5
3 or 0    3
0 or 0    0

a=3 
b=5
print(a>2 or b>9) 
print(a<2 or b>9) 
print(a>2 or b<9) 
print(a<2 or b<9) 
o/p:
True
False
True
True


and
op1     op2      result
True    True      True
True    False     False
False    True     False
False    False     False

print(True and False)  #False

if first operand is true  second operand must checking.
if first operand  is false  second operand not checking
any nonzero value    True 

3 and 5    5
0 and  5   0
3 and 0    0
0 and 0    0

a=3 
b=5
print(a>2 and b>9) 
print(a<2 and b>9) 
print(a>2 and b<9) 

o/p:
False
False
True





not 
____


operand   resulet

True       False
False       True


not True    False
not False   True

print(not True)
print(not False)
print( not 5)
print(not not 5)

o/p:

False
True
False
True


identity operator
____________________
is      compare reference
is not

==    compare value

a=10
b=10
c=20
print(a is b)
print(a is c)
print(a is not c)
print(a==b)

o/p:
True
False
True
True

a=[10]
b=[10]
c=[20]
print(a is b)
print(a is c)
print(a is not c)
print(a==b)


o/p:
False
False
True
True


membership operator (in ,not in)

print("n" in "india")  #True
print("ndi" in "india")  #True
print("x" in "india")  #False
print("x" not in "india")  #True
print(10  in [5,7,10,12,34])  #True
print(30  in [5,7,10,12,34])  #False
print(30  not in [5,7,10,12,34])  #True








assginment  operator

  vname =vname/constant/expression
  a=10
  b=20
  10=a  invalid
  10=20  invalid
  a+b=30  invalid

swapping two no using 3rd variable

a=10
b=20
temp=b
b=a
a=temp
print(a,b)

o/p:
20 10


swapping two no without using  3rd variable
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)
or
a=10
b=20
a=a*b
b=a//b
a=a//b
print(a,b)
or
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)



a=10
b=20
a,b=b,a   #(only python)
print(a,b)



compund assginment operator
____________________________

+=
-=
*=
/=
%=
//=
**=
&=
|=
^=
<<=
>>=

a+=3    a=a+3
b*=3   b=b*3

10+=2    error   10=10+2

a+=b*=c+=2   error  (in python)     valid c c++ java

#wap take student name rollno and mark display it
print("enter student name rollno and mark ")
nm=input()
r=int(input())
m=float(input())
print("name=",nm)
print("rollno=",r)
print("mark=",m)
o/p:
enter student name rollno and mark
muna das
1
90.50
name=muna das
rollno=1
mark=90.50

#wap take rectangle length and breadth from keyboard displAY LENGTH 
#breadth  area and perimeter.
print("enter rectagle length ")
L=float(input())
print("enter rectagle breadth ")
B=float(input())
ar=L*B
pr=2*(L+B)
print("length=",L)
print("breadth=",B)
print("area=",ar)
print("perimeter=",pr)

o/p:
enter rectangle length
3.5
enter rectangle breadth
4.5
length=3.5
breadth=4.5
area=
perimeetr=


#simple interset
#sal da ta